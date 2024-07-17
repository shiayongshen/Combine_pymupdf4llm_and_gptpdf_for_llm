import os
import re
from typing import List, Tuple, Optional, Dict
import logging
from IPython.display import HTML, display
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
import fitz  # PyMuPDF
import shapely.geometry as sg
from shapely.geometry.base import BaseGeometry
from shapely.validation import explain_validity
import concurrent.futures
from GeneralAgent import Agent
api_key = 'your-key'
model = 'gpt-4o'
role_prompt = """
"""
local_prompt = """
"""
rec_prompt = """
"""
def preprocess(
        pymupdf_content: str,
        pymupdf_table_list: List[Dict],
        image_path: List[str],
        rects:List[List[Tuple]],
        embedding_function: str,
        output_dir: str = './chroma_db'
) -> str:
    import re
    role_prompt = """你是一個圖片摘要生成的機器人
"""
    local_prompt = """你是一個圖片摘要生成的機器人
"""
    rec_prompt = """
"""
    def filter_table(content:str)-> List[str]:
        table_pattern = re.compile(
        r'(\|(?:[^\n]*\|)+\n'   # 匹配表格头部行
        r'\|(?:\s*[-:]+\s*\|)+\s*\n'  # 匹配表格分隔行
        r'(?:\|(?:[^\n]*\|)\n)+)'  # 匹配表格内容行
        )
        result = table_pattern.findall(content)
        return result
    
    def init_chroma(embedding_function,output_dir):
        return 0
    #utilize image and table 
    for index,i in enumerate(pymupdf_table_list):
        if i['tables'] !=[] and i['images']!= []: #圖片表格都存在
            #比對座標來判斷是否為表格
            table_markdown = filter_table(i['text'])
            image_list = [filename for filename in image_path if filename.startswith(str(index)+'_')]
            table_list = []
            print(index)
            rect = rects[index]  #取出gptpdf座標
            for j in i['tables']:
                for ind,k in enumerate(rect):
                    contract = (j['bbox'][1] - k[1]) + (j['bbox'][0]-k[0])
                    #rect_h_l = (k[2]-k[0])+(k[3]-k[1])
                    #pymu_h_l = (j['bbox'][2]-j['bbox'][0])+(j['bbox'][3]-j['bbox'][1])
                    #if (abs(rect_h_l-pymu_h_l)) < 30 and (abs(k[0]-j[0]))<30:
                    if (abs(contract) < 40):
                        path = str(index) + '_' + str(ind) +'.png'
                        image_list.remove(path)
                        table_list.append(path)
            for inde,m in enumerate(table_list):
                print("table:")
                print(m)
                table_role_prompt= """
                你現在是一位專注於製作HTML表格的工程師，你的任務是要畫出一個可以顯示的表格。
                """
                table_local_prompt = """
                你現在是一個製作HTML表格的工程師，你的任務是將圖片中表格的架構以及markdown的表格中的內容作結合，你必須要做到:
                1.請專注在圖片表格的結構，完整的表現出原本的架構。
                2.請使用Markdown中的文字來填入表格中。
                3.請注意合併儲存格，讓結構完整。                
                """
                agent = Agent(role=table_role_prompt, api_key=api_key, base_url=None, model=model, disable_python_run=False)
                local_prompt = table_local_prompt + table_markdown[inde]
                content = agent.run([local_prompt, {'image': 'pic/'+m}])
            for inde_n,n in enumerate(image_list):
                print("image:")
                print(n)
                role_prompt = """你是一個圖片摘要生成的機器人
                """
                local_prompt = """你是一個圖片摘要生成的機器人
                """
                agent = Agent(role=role_prompt, api_key=api_key, base_url=None, model=model, disable_python_run=False)
                local_prompt = local_prompt
                content = agent.run([local_prompt, {'image': 'pic/'+n}])

        elif i['tables'] == [] and i['images']!= []: #只有圖片
            #看有幾張圖片
            image_list = [filename for filename in image_path if filename.startswith(str(index)+'_')]
            for j in image_list:
                print("image:",j)
                role_prompt = """你是一個圖片摘要生成的機器人
                """
                local_prompt = """你是一個圖片摘要生成的機器人
                """
               #call llm
                agent = Agent(role=role_prompt, api_key=api_key, base_url=None, model=model, disable_python_run=False)
                local_prompt = local_prompt
                content = agent.run([local_prompt, {'image':'pic/'+j}])
        elif i['tables'] != [] and i['images'] == []: #只有表格
            #看有幾個表格 
            table_role_prompt= """
            你現在是一位專注於製作HTML表格的工程師，你的任務是要畫出一個可以顯示的表格。
            """
            table_local_prompt = """
            你現在是一個製作HTML表格的工程師，你的任務是將圖片中表格的架構以及markdown的表格中的內容作結合，你必須要做到:
            1.請專注在圖片表格的結構，完整的表現出原本的架構。
            2.請使用Markdown中的文字來填入表格中。
            3.請注意合併儲存格，讓結構完整。                
            """
            image_list = [filename for filename in image_path if filename.startswith(str(index)+'_')]
            table_markdown = filter_table(i['text'])
            for j in table_markdown:  #將純文本表格去除
                pymupdf_content = pymupdf_content.replace(j,'')
            for k in image_list:
                print("table:",k)
                #call llm
                agent = Agent(role=table_role_prompt, api_key=api_key, base_url=None, model=model, disable_python_run=False)
                local_prompt = table_local_prompt + table_markdown
                content = agent.run([local_prompt, {'image': 'pic/'+k}])

"""
扩展内容：
1，抓取人力资源管理系统的员工列表接口（抓取方法， 在有大量员工的页面刷新页面，就能通过抓包工具抓取到员工列表接口了）
2，使用代码调用员工列表接口并打印出员工列表的数据
"""
import requests

session = requests.Session()

session.post('http://182.92.81.159/api/sys/login',json={"mobile": "13800000002", "password": "123456"})
response = session.get('http://182.92.81.159/api/sys/user?page=1&size=10')

print(response.json())


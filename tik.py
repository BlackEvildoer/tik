import requests
from user_agent import generate_user_agent
def user_info():
	user = input("USER NAME :\n")
	sw = input("SESSION ID :\n")
	headers = {
		'Host': 'www.tiktok.com',
		'Cookie': f'sessionid={sw}',
		'User-Agent': 'Mozilla/5.0 (Linux; Android 10)'}
	response = requests.get(f'https://www.tiktok.com/api/uniqueid/check/?unique_id={user}&aid=1233&app_name=tiktok_web&device_platform=web_mobile&region=SA&os=android&screen_width=360&screen_height=780&browser_language=ar-SA&browser_platform=Linux&browser_name=Mozilla&browser_version=5.0%20%28Linux%3B%20Android%2010%3B%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F90.0.4430.82%20Mobile%20Safari%2F537.36&browser_online=true&timezone_name=Asia%2FRiyadh&_signature=_02B4Z6wo00101kZaPigAAIDAAT3gcnLW59ZGWjqAAPFm46',
		headers=headers)
	print("LOGIN SUCSUSFULL")
	print(response.text)
def session_info():
    sid3=input("Enter your session id:\n")
    postid="6963920485398744321"
    tx=input("Enter a random text:\n")
    url = f"https://www.tiktok.com/api/comment/publish/?aid=1988&app_name=tiktok_web&device_platform=web&referer=https:%2F%2Fwww.tiktok.com%2F&root_referer=https:%2F%2Fwww.tiktok.com%2F&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F90.0.4430.93+Safari%2F537.36&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=ar&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F90.0.4430.93+Safari%2F537.36&browser_online=true&ac=4g&timezone_name=Asia%2FBahrain&priority_region=BH&verifyFp=verify_kmwy2hf4_AmVogh0N_Tkne_4BpA_ANSq_9oOueM2pIh3s&appId=1233&region=BH&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=windows&did=6944589237636646401&tt-web-region=BH&uid=6957894826579641349&aweme_id={postid}&text={tx}&device_id=6944589237636646401&_signature=_02B4Z6wo00101xegn7AAAIDAKCYplETPOLsXoJsAAKVx98"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.tiktok.com',
        f'cookie': f'tt_webid_v2=6944589237636646401; tt_webid=6944589237636646401; s_v_web_id=verify_kmwy2hf4_AmVogh0N_Tkne_4BpA_ANSq_9oOueM2pIh3s; tt_csrf_token=dQmMg8Uekbw2Oq3qWeMzmZPV; csrf_session_id=53caf56337014635982064c815fd0b40; R6kq3TV7=APBQKTB5AQAARUF0d_OQ-94UVu51UTkJV6aMnxLDIekq-bfbknTR1okfl63_|1|0|27675acbbb7f3bf62040a83a6038ebc361ab9539; ak_bmsc=1C37B7EFB848AACA78C6A86D2E98F4472E2A548E28340000BD668F60218C611A~plMf9kvndtWdGMYA6ntojGLjZAnbo9JL/O3k0tlMDA/bnO2xhgSlQPPClh0dOgGSaun5sLRBrfmGZ2EZStGoGE8ZvuGNl7JDdOJ+vMkSPg8ONxn/pue9pK75OI1uenyR8+BSuBg0l/4nl8Gkz2mC4jTKnu2W8fm8vyijAPGEy9dHMGeHevdaKji8TeHmTmmz+qIM2AqFZBgMiLtpZqfNfN3vFoeaojuT1oOXdwCP/j6P4=; bm_sz=F2EFD804894550F3CA53C6456C64DB72~YAAQjlQqLhK1DiB5AQAA/1MpMAudG6Do3bfpbNxInp+UTsyWegkW8B64MgSviKu0pp5V6Fhluh66SzeqUvOsChOxFC+JDudD3O+1JSYqWBdunXgsvsM1RiFfvonoaen5R1R+Y0DbcTkKaCo/9sii4e9IYFF6icxq+NHilHnVzugyLNeBoXWWdMejkyg1M6bJ; _abck=D689B4F48527BC79C2A79217632F331E~0~YAAQjlQqLhO1DiB5AQAA/1MpMAVWkY7o8DGEfut8tpMTkcOrYGsuzI00y8cmKO/os7ywHsi5UeafSAqlHSEyTY8wbVoei6XMgYICIMnoZ8tCQe8nzK9j3h5K+aYRq+C7U7YFp0vToH1HZBDYtynCuZqOmKSoZ5CymLYStP97xIyliQ2+hOFddb2GUSlZ/p4lSupiCDj3XximHvlm7r746WAF3MBJC4JAqedluFI3UkebwX8A87Y3DDK4iAqVeDyKLjlKJ2scqw/5anKng648GEBMYJr2Sx1M8Ph6bct1qCSMXsm/lUlJMXn9YHxMXnM9tSCgovhpCSjHokc3o1DXebuNR+BWl4FDeZ3rdMMec+Mrf7UbHWapraXB7V1hRyI2dSIAlG86Mg6PFL79KgGmpQ8PQuD2q30t~-1~-1~-1; passport_csrf_token=45de29b0fdd44543ae03ebca1712aba9; passport_csrf_token_default=45de29b0fdd44543ae03ebca1712aba9; ttwid=1%7C76-Am_AM-jdvsHzB1lr6PLsnCSwMEQmDmftstnJM4c4%7C1620011314%7C98e8f2f8df0f69b0d8133eab649605fa3487dba3c89a7632aaeeddd6b8b0ed51; sid_guard={sid3}%7C1620011343%7C5184000%7CFri%2C+02-Jul-2021+03%3A09%3A03+GMT; uid_tt=1cb4ab185b6df7ced107550b73cba72dc6ae4d5d36a5b360202bf9712f73db6e; uid_tt_ss=1cb4ab185b6df7ced107550b73cba72dc6ae4d5d36a5b360202bf9712f73db6e; sid_tt={sid3}; sessionid={sid3}; sessionid_ss={sid3}; store-idc=alisg; store-country-code=bh; cmpl_token=AgQQAPNZF-RMpbCxht16_B08-gG6LbPKf4PSYPhliQ; MONITOR_WEB_ID=6944589237636646401; odin_tt=a0e48820809040f306cc53f7c451b11dc8b0dcc1a0a154e9aa47bc3b460120ce2073a7979a3ba19fd724b00c8968968fd494a2299079c4607d3d3d5fdcbd1a12996f7fc7e82bc35ba3623247430e4e58; bm_sv=313B67CA31A48965C7AAD5944033B58E~Lso3XobClkO+2LgPELng8uvbHFQCpeycIWyhPae5NVMiuMlyoz2pWZbwQ6Z6gAO5arGhNfLqdCy0HQaYdIdEQanEAPwyfc0vmFH4fXTNkKg9xGR3OVK9Euo8BXuHIw3clCQpN6/kAXDBufMKkXmOhTF55BEqEYKxm+UDNHlZYAo=',
        'referer': f'https://www.tiktok.com/@volleyboll_dear/video/{postid}?is_copy_url=1&is_from_webapp=v1',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'tt-csrf-token': 'dQmMg8Uekbw2Oq3qWeMzmZPV',
        'user-agent': generate_user_agent()}
    req = requests.post(url, headers=headers)
    a1 = str(req.json()["status_msg"])
    a2 = str(req.json()["status_code"])
    a3 = str(req.json()["comment"])
    print(a1,a2,a3)
choose=int(input("1) USER INFO\n2) SESSION ID INFO\n-->"))
if choose==1:
    user_info()
elif choose==2:
    session_info()

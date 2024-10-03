######### - Libs - #########
import requests , random ,  time ; from MedoSigner import Argus,Gorgon, md5,Ladon ; from urllib.parse import urlencode ; from os import system


def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        data=payload
        if not unix: unix = int(time.time())
        return Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : Ladon.encrypt(unix, license_id, aid),"x-argus"   : Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}
def unix(spoof: int = 0) -> str:
        if spoof == 0:
            _unix = str(int(time.time()))
        else:
            _unix = str(round(time.time(), spoof)).replace(".", "")
        return _unix

cookies = {
  "passport_csrf_token": "7536cf642186839257927701f2e47f77",
  "passport_csrf_token_default": "7536cf642186839257927701f2e47f77",
  "d_ticket": "13a1fb94f87096561623cc6ba8d87097523d0",
  "multi_sids": "7325282234032948270%3A1f6aa7e4a2ee33d47941d6ebf0389ecf",
  "odin_tt": "de0251ca39a44ba0fbdd3e3d7e9b096e14947d140a7664c75c4e063628aceeebdac5ae561f79a858db4dc6e9f31c3b5f2944f09988777dcbb6bb5ca346adfc8019ede4b0bf3512313c9d401793724844",
  "cmpl_token": "AgQQAPNSF-RPsLWWT8b3MV0X_9mMF3XPf4csYNV1gA",
  "sid_guard": "1f6aa7e4a2ee33d47941d6ebf0389ecf%7C1725933393%7C5184000%7CSat%2C+09-Nov-2024+01%3A56%3A33+GMT",
  "uid_tt": "a9d47d1c0db42c2edeb62218570ac3b83f551f71a89af8f0788d21f95f800950",
  "uid_tt_ss": "a9d47d1c0db42c2edeb62218570ac3b83f551f71a89af8f0788d21f95f800950",
  "sid_tt": "1f6aa7e4a2ee33d47941d6ebf0389ecf",
  "sessionid": "1f6aa7e4a2ee33d47941d6ebf0389ecf",
  "sessionid_ss": "1f6aa7e4a2ee33d47941d6ebf0389ecf",
  "store-idc": "useast5",
  "store-country-code": "us",
  "store-country-code-src": "uid",
  "tt-target-idc": "useast5",
  "install_id": "7410643359179917098",
  "ttreq": "1$7d178ea887ed77f5a454aaa40eee1d293672fc92",
  "msToken": "uYLK0uICkUCeLTPRBISv7UGPeCQ4sp4Wkw2zDL_-C3BsDajtwUQO6UkH_otTetm0OzcN6miTFLYCbULQKlkz-8JtqIVX9wA0Fjdx2R0ebkTbyOtDPVn-VJjlCQ6I"
}
 
 
 
def chk(user):
  m=sign(params=f"unique_id={user}&device_platform=android&os=android&ssmix=a&_rticket=1725979888760&cdid=32fcca4c-2054-4e68-b3a1-20c532daa279&channel=googleplay&aid=1233&app_name=musical_ly&version_code=350304&version_name=35.3.4&manifest_version_code=2023503040&update_version_code=2023503040&ab_version=35.3.4&resolution=1440*2969&dpi=532&device_type=SM-S928B&device_brand=samsung&language=ar&os_api=34&os_version=14&ac=wifi&is_pad=0&current_region=IQ&app_type=normal&sys_region=AE&last_install_time=1725879126&mcc_mnc=41820&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&residence=IQ&app_language=ar&carrier_region=IQ&timezone_offset=10800&host_abi=arm64-v8a&locale=ar&ac2=wifi&uoo=0&op_region=IQ&build_number=35.3.4&region=AE&ts=1725979887&iid=7410643359179917098&device_id=7363585065539798574&openudid=d734f4604840e801",payload="",cookie=cookies)
  headers = {'User-Agent': "com.zhiliaoapp.musically/2023503040 (Linux; U; Android 14; ar_AE; SM-S928B; Build/UP1A.231005.007; Cronet/TTNetVersion:711894ae 2024-06-04 QuicVersion:5f987023 2024-05-10)",'x-argus': m["x-argus"],  'x-gorgon':m["x-gorgon"],'x-khronos': m["x-khronos"],'x-ladon':m["x-ladon"],'Cookie': "passport_csrf_token=7536cf642186839257927701f2e47f77; passport_csrf_token_default=7536cf642186839257927701f2e47f77; d_ticket=13a1fb94f87096561623cc6ba8d87097523d0; multi_sids=7325282234032948270%3A1f6aa7e4a2ee33d47941d6ebf0389ecf; odin_tt=de0251ca39a44ba0fbdd3e3d7e9b096e14947d140a7664c75c4e063628aceeebdac5ae561f79a858db4dc6e9f31c3b5f2944f09988777dcbb6bb5ca346adfc8019ede4b0bf3512313c9d401793724844; cmpl_token=AgQQAPNSF-RPsLWWT8b3MV0X_9mMF3XPf4csYNV1gA;
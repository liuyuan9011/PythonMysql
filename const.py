# -*- coding:utf-8 -*-

DEFAULT_READ_TIMEOUT = 20
DEFAULT_INSERT_NUM = 1000
MERCHANT_FILE = './merchant_id.txt'


class DbConfig(object):
    host = '10.6.19.35'
    port = 3307
    password = '7SmflrViu9Wk8IFi_t5rYoJXtZVfL4NF'
    user = 'people_t_w'
    db_name = 'engagement_survey'



# 需要一次传入biz_id和merchant_id两个参数
SQL_FORMAT_1 = '''
insert into global_apply_order(tnt_inst_id, biz_id, gmt_create, gmt_modified, out_biz_no, order_type, 
order_content, order_status, creator_id, creator, ext_info, region_code, version, biz_status, 
target_id, source_id, biz_scene) 
values 
('ALIPW3LU', '%s', '2019-06-14 06:07:43', '2019-06-14 06:07:43', '2019061411089100000002300174773', 'MERCHANT_CONTRACT_APPLY', 
'{"balanceAccountInfo":{"currencies":["EUR"]},"deviceInfo":{"clientIp":"121.0.29.220","clientUmid":"CV11u5c08ba1a541048d70007653e0d9c","language":"th_TH","osType":"ipad","osVersion":"8.5.0","sessionId":"26daf780047938bf8d5b7ea8906003e9","terminalType":"APP","tokenId":"O/MtqlrKCmggEPO7ZECwOYmF8eep4arkbJT8u6rILBM3KeqoVAEAAA=="},"merchantInfo":{"attachmentInfoList":[{"attaName":"公司章程附件","attaType":"LOGO","attaUrl":"2019061400089IMERCHPRODe7aee1533557c6ae3e0bcaf970744b39_公司章程附件"}],"businessInfo":{"mcc":"4125","sourceOfWealth":["OTHERS"]},"certificateInfoList":[{"certificateAttamentList":[{"attaName":"zhangsan","attaType":"PASSPORT","attaUrl":"2019061400089IMERCHPROD4e71a9784da75067ca2cd43e7b156d09_zhangsan"}],"certificateNo":"1234567890","certificateType":"PASSPORT","effectiveDate":1536508800000,"expireDate":1599667200000,"holderName":"zhangsan","validType":"FIXED_TERM"}],"contactPersonInfoList":[{"certificateInfoList":[{"certificateAttamentList":[{"attaName":"zhangsan","attaType":"PASSPORT","attaUrl":"2019061400089IMERCHPROD8376c3ae974f109ad4d7383c9356df87_zhangsan"}],"certificateNo":"1234567890","certificateType":"PASSPORT","effectiveDate":1536508800000,"expireDate":1599667200000,"holderName":"zhangsan","validType":"FIXED_TERM"}],"contactPersonType":"COMMON","dateOfBirth":1539144000000,"department":"departmentA","email":"sample@qq.com","fullName":"name","nationality":"US","phoneNo":"1351111122132","placeOfBirth":{"detailAddress":"JAPAN"},"positon":"CEO","residentAddress":{"detailAddress":"any place"},"residentRegion":"US","shareholdingRatio":"5"}],"instBusinessInfoList":[{"businessCode":"FUND","instId":"Z06","subBusinessCode":"B_FUND","validStatus":"F"},{"businessCode":"PAY","instId":"Z06","subBusinessCode":"ONLINE_PAY","validStatus":"F"}],"labelInfoList":[{"name":"COMMON_GLOBAL_AGH_AE_SELLER"},{"name":"INTNL_MCT_B_FUND_NORMAL"}],"merchantBaseInfo":{"bizSource":"AE","contactEmail":"abc11@alipay.com","externalMerchantId":"AE_seller_xh_012","gka":false,"loginId":"ab111c@alipay.com","merchantId":"%s","merchantType":"ENTERPRISE","name":"xxx","onboardChannel":"ALIBABA","operationAddress":{"detailAddress":"杭州蚂蚁Z空间"},"parentMerchantId":"2190400000000015","registrationAddressInfo":{"detailAddress":"xxx","region":"FR"},"registrationDate":1536508800000,"registrationNo":"AE_2190110000082734_5645634534","registrationType":"JP_REGISTRATION","roleType":"MERCHANT","specialApproved":false,"taxNo":"US000034","testAccount":false,"vatNo":"123123123123123"},"relAccountInfoList":[{"accountNo":"2088xxx","accountSource":"ALIPAY","accountType":"OTHER_SITE_ACCOUNT"}]},"requestId":"SX_0000012"}', 'INIT', null, null, '{"sourceId":"AE_seller_xh_012","bizIdentify":"AE_ASYNC_CONTRACT_SIGN","processorList":["ONBOARD_APPLY","ONBOARD_KYB_RISK_AUDIT","ONBOARD_KYB_FINISH","ONBOARD_KYC_APPLY"],"riskReportConsultResult":"{\\"agreementEntity\\":\\"Z06\\",\\"businessCode\\":\\"FUND\\",\\"entryId\\":\\"2019061411089100000002300174773\\",\\"errorCodes\\":[],\\"extendInfo\\":{},\\"gmtCreate\\":1560506716045,\\"gmtModified\\":1560506716045,\\"merchantId\\":\\"2190110000082734\\",\\"needRectify\\":false,\\"riskResult\\":\\"ACCEPT\\",\\"subBusinessCode\\":\\"B_FUND\\",\\"version\\":1}","isNewUser":true,"alipayId":"2088xxx","registerBizCode":"NORMAL"}', 
'1', 1, null, null, null, 'AE');
'''

# 需要传入biz_id参数，且和SQL1的biz_id绑定
SQL_FORMAT_2 = '''
insert into `global_common_async_task`(task_id, gmt_create, gmt_modified, tnt_inst_id, biz_id, task_type, task_status, 
retry_times, next_execute_time, region_code, ext_info, fail_reason, env) 
values 
('2019061411089102000002700118364', '2019-06-14 06:07:43', '2019-06-15 04:57:28', 'ALIPW3LU', '%s', 'MERCHANT_CONTRACT_SIGN', 
'INIT', 0, '2019-06-14 12:11:43', '1', '', '', '');
'''

TEST_SQL = '''
SELECT VERSION()
'''
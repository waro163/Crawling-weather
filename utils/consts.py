#coding=utf-8
class HEWEAPI():
	''' official website https://www.heweather.com '''
	KEY = '9e6824edf3e54b9bacb27c7a6e3441cf'  # API key
	
	LOCATION_CODE = 'CN101030500'
	LOCATION_ENG_NAME = 'xiqing'
	LOCATION_CH_NAME = '西青'
	
	URL_API = 'https://api.heweather.com/v5/now'  # pay API URL
	URL_FREE_API = 'https://free-api.heweather.com/v5/now' #free API
	
	LANGUAGE = 'en'  # return result language
	SIMP_CH_LANG = 'zh'
	TRAD_CH_LANG = 'hk'
	ENG_LANG = 'en'
	GERM_LANG = 'de'
	SPAN_LANG = 'es'
	FRAN_LANG = 'fr'
	ITLY_LANG = 'it'
	JPAN_LANG = 'jp'
	KOREA_LANG = 'kr'
	RUSS_LANG = 'ru'
	INDIA_LANG = 'in'
	THAI_LANG = 'th'
	
	ERROR_INFO = {'invalid key':'错误的key',
					'unknown city':'未知或错误城市',
					'no more requests':'超过访问次数',
					'param invalid':'参数错误',
					'too fast':'超过限定的QPM',
					'anr':'无响应或超时',
					'permission denied':'无访问权限，如免费key强制获取付费数据或获取未购买的付费数据'
					}
	STATUS_INFO = {'ok':'数据正常'}
#	STATUS_INFO.update(ERROR_INFO)
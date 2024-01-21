'''Baidu Translation'''

'''
This program cannot be run directly.
Some code is replaced by '***'.
One of reasons is to be train yourself.
Try to fill the blanks if you want to improve your skills.
'''

import requests
import re
import js2py

langList = {
    'zh': 'Chinese', 'jp': 'Japanese', 'jpka': 'Japanese kana', 'th': 'Thai', 'fra': 'French', 'en': 'English', 'spa': 'Spanish',
    'kor': 'Korean', 'tr': 'Turkish', 'vie': 'Vietnamese', 'ms': 'Malay', 'de': 'German', 'ru': 'Russian', 'ir': 'Iranian',
    'ara': 'Arabic', 'est': 'Estonian', 'be': 'Belarusian', 'bul': 'Bulgarian', 'hi': 'Hindi', 'is': 'Icelandic',
    'pl': 'Polish', 'fa': 'Persian', 'dan': 'Danish', 'tl': 'Filipino', 'fin': 'Finnish', 'nl': 'Dutch',
    'ca': 'Catalan', 'cs': 'Czech', 'hr': 'Croatian', 'lv': 'Latvian', 'lt': 'Lithuanian', 'rom': 'Romanian',
    'af': 'South African', 'no': 'Norwegian', 'pt_BR': 'Brazilian', 'pt': 'Portuguese', 'swe': 'Swedish', 'sr': 'Serbian',
    'eo': 'Esperanto', 'sk': 'Slovak', 'slo': 'Slovenian', 'sw': 'Swahili', 'uk': 'Ukrainian', 'iw': 'Hebrew',
    'el': 'Greek', 'hu': 'Hungarian', 'hy': 'Armenian', 'it': 'Italian', 'id': 'Indonesian', 'sq': 'Albanian',
    'am': 'Amharic', 'as': 'Assam', 'az': 'Azerbaijani', 'eu': 'Basque', 'bn': 'Bengali', 'bs': 'Bosnian',
    'gl': 'Galician', 'ka': 'Georgian', 'gu': 'Gujarati', 'ha': 'Hausa', 'ig': 'Ibo', 'iu': 'Inuit',
    'ga': 'Irish', 'zu': 'Zulu', 'kn': 'Kanada', 'kk': 'Kazakh', 'ky': 'Kyrgyz', 'lb': 'Luxembourg',
    'mk': 'Macedonian', 'mt': 'Maltese', 'mi': 'Maori', 'mr': 'Malati', 'ne': 'Nepali', 'or': 'Olya',
    'pa': 'Punjabi', 'qu': 'Kechua', 'tn': 'Setswana', 'si': 'Sinhalese', 'ta': 'Tamil', 'tt': 'Tatar',
    'te': 'Telugu', 'ur': 'Urdu', 'uz': 'Uzbek', 'cy': 'Welsh', 'yo': 'Yoruba', 'yue': 'Cantonese',
    'wyw': 'Classical Chinese', 'cht': 'Traditional Chinese',
}  # some cannot be translated... with unknown reasons

sess = requests.Session()

headers = {
    'User-Agent': '***',  # replace *** with valid one
    'Referer': 'https://fanyi.baidu.com'
}


def get_token():
    url_ = 'https://fanyi.baidu.com'
    while True:  # the first attempt may fail
        res_ = sess.get(url_, headers=headers)
        token_ = re.findall(r"(***)", res_.text)[0]  # get token  # replace "(***)" with "token: '(.*?)',"
        gtk_ = re.findall(r'(***)', res_.text)[0]  # get gtk  # replace '(***)' with 'window.gtk = "(.*?)";'
        if len(token_) != 0: return [token_, gtk_]
        else: print(f'Token fetch failure，Retrying...')


def detect(lan_: str):  # auto detect input language
    url_ = 'https://fanyi.baidu.com/langdetect'
    data_ = {'query': lan_}
    try:
        res_ = sess.post(url_, data_)
        js_ = res_.json()
        if 'msg' in js_ and js_['msg'] == 'success': return js_['lan']
    except Exception as e:
        print(f'Error - {e}')
        return None


def translate(to_lan: str = 'zh'):
    word = input('Input content to translate:')
    if word == '': quit()  # input nothing to shut the window down
    from_lan = detect(word)  # detect input language
    token, gtk = get_token()  # get token and gtk
    # important js code to calculate some values
    js_txt = r'''
            function e(t, e) {
                (null == e || e > t.length) && (e = t.length);
                for (var n = 0, r = new Array(e); n < e; n++)
                    r[n] = t[n];
                return r
            }
            function n(t, e) {
                for (var n = 0; n < e.length - 2; n += 3) {
                    var r = e.charAt(n + 2);
                    r = "a" <= r ? r.charCodeAt(0) - 87 : Number(r),
                    r = "+" === e.charAt(n + 1) ? t >>> r : t << r,
                    t = "+" === e.charAt(n) ? t + r & 4294967295 : t ^ r
                }
                return t
            }
            r = "320305.131321201"
            function aa(t) {
                var o, i = t.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
                if (null === i) {
                    var a = t.length;
                    a > 30 && (t = "".concat(t.substr(0, 10)).concat(t.substr(Math.floor(a / 2) - 5, 10)).concat(t.substr(-10, 10)))
                } else {
                    for (var s = t.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), c = 0, u = s.length, l = []; c < u; c++)
                        "" !== s[c] && l.push.apply(l, function(t) {
                            if (Array.isArray(t))
                                return e(t)
                        }(o = s[c].split("")) || function(t) {
                            if ("undefined" != typeof Symbol && null != t[Symbol.iterator] || null != t["@@iterator"])
                                return Array.from(t)
                        }(o) || function(t, n) {
                            if (t) {
                                if ("string" == typeof t)
                                    return e(t, n);
                                var r = Object.prototype.toString.call(t).slice(8, -1);
                                return "Object" === r && t.constructor && (r = t.constructor.name),
                                "Map" === r || "Set" === r ? Array.from(t) : "Arguments" === r || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r) ? e(t, n) : void 0
                            }
                        }(o) || function() {
                            throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                        }()),
                        c !== u - 1 && l.push(i[c]);
                    var p = l.length;
                    p > 30 && (t = l.slice(0, 10).join("") + l.slice(Math.floor(p / 2) - 5, Math.floor(p / 2) + 5).join("") + l.slice(-10).join(""))
                }
                for (var d = "".concat(String.fromCharCode(103)).concat(String.fromCharCode(116)).concat(String.fromCharCode(107)), h = (null !== r ? r : (r = window[d] || "") || "").split("."), f = Number(h[0]) || 0, m = Number(h[1]) || 0, g = [], y = 0, v = 0; v < t.length; v++) {
                    var _ = t.charCodeAt(v);
                    _ < 128 ? g[y++] = _ : (_ < 2048 ? g[y++] = _ >> 6 | 192 : (55296 == (64512 & _) && v + 1 < t.length && 56320 == (64512 & t.charCodeAt(v + 1)) ? (_ = 65536 + ((1023 & _) << 10) + (1023 & t.charCodeAt(++v)),
                    g[y++] = _ >> 18 | 240,
                    g[y++] = _ >> 12 & 63 | 128) : g[y++] = _ >> 12 | 224,
                    g[y++] = _ >> 6 & 63 | 128),
                    g[y++] = 63 & _ | 128)
                }
                for (var b = f, w = "".concat(String.fromCharCode(43)).concat(String.fromCharCode(45)).concat(String.fromCharCode(97)) + "".concat(String.fromCharCode(94)).concat(String.fromCharCode(43)).concat(String.fromCharCode(54)), k = "".concat(String.fromCharCode(43)).concat(String.fromCharCode(45)).concat(String.fromCharCode(51)) + "".concat(String.fromCharCode(94)).concat(String.fromCharCode(43)).concat(String.fromCharCode(98)) + "".concat(String.fromCharCode(43)).concat(String.fromCharCode(45)).concat(String.fromCharCode(102)), x = 0; x < g.length; x++)
                    b = n(b += g[x], w);
                return b = n(b, k),
                (b ^= m) < 0 && (b = 2147483648 + (2147483647 & b)),
                "".concat((b %= 1e6).toString(), ".").concat(b ^ f)
            }
    '''
    js = js2py.EvalJs()
    js.execute(js_txt)
    sign = js.aa(word)  # get sign value with js code
    data = {
        'from': from_lan,
        'to': to_lan,
        'query': word,
        'simple_means_flag': '3',
        'sign': sign,
        'token': token
    }
    url = f'https://fanyi.baidu.com/v2transapi'
    res = sess.post(url, headers=headers, data=data)
    result = re.findall(r'(***)', res.text)[0]  # replace '(***)' with '"dst":"([^{]*?)",'
    print(result.encode('utf-8').decode('unicode_escape'))  # in case unrecognizable code


def main():
    print(langList)  # list languages available to translate
    to_ = input('Translate into [zh/en/jp/...]:')
    while True:
        if to_ not in langList: to_ = input('Language unsupported，Please retry:')
        else: break
    try:
        while True: translate(to_)
    except KeyboardInterrupt: return None


if __name__ == '__main__':
    main()
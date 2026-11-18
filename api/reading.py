import os, json, re, hmac
from http.server import BaseHTTPRequestHandler
from openai import OpenAI

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        secret=os.getenv('DALBIT_ACCESS_CODE','')
        if not secret or not hmac.compare_digest(self.headers.get('X-Dalbit-Access',''), secret):
            return self.send_json(403,{'detail':'테스트 접속 코드가 올바르지 않습니다.'})
        if not os.getenv('OPENAI_API_KEY'):
            return self.send_json(503,{'detail':'서버에 OpenAI API 키가 아직 등록되지 않았습니다.'})
        try:
            length=int(self.headers.get('Content-Length','0'))
            if length < 2 or length > 4096: return self.send_json(400,{'detail':'입력 크기를 확인해주세요.'})
            data=json.loads(self.rfile.read(length))
            birth=str(data.get('birth',''))
            if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',birth):return self.send_json(400,{'detail':'생년월일을 입력해주세요.'})
            topic=str(data.get('topic',''))[:80]
            prompt=f'''주제: {topic}\n생년월일: {birth}\n달력: {str(data.get('calendar',''))[:20]}\n출생시각: {str(data.get('birth_time') or '미상')[:20]}\n검증된 만세력 계산 결과가 제공되지 않았으므로 사주팔자·일주·신살·대운 등을 계산하거나 추정하지 마세요. 전통 명리학에서 해당 주제를 어떻게 해석하는지, 필요한 계산 정보, 실생활에 참고할 일반적인 조언을 한국어로 5개 소제목으로 자세히 작성하세요. 미래를 확정적으로 예언하거나 불안·결제를 조장하지 마세요. 전통문화 기반 오락 및 자기성찰용임을 분명히 밝혀주세요.'''
            response=OpenAI(timeout=25).responses.create(model=os.getenv('OPENAI_MODEL','gpt-4.1-mini'),input=prompt,max_output_tokens=1600)
            return self.send_json(200,{'text':response.output_text,'verified_manse':False})
        except Exception:
            return self.send_json(502,{'detail':'AI 요청에 실패했습니다. 잔액 및 서버 설정을 확인해주세요.'})
    def send_json(self,status,data):
        payload=json.dumps(data,ensure_ascii=False).encode()
        self.send_response(status);self.send_header('Content-Type','application/json; charset=utf-8');self.send_header('Cache-Control','no-store');self.send_header('Content-Length',str(len(payload)));self.end_headers();self.wfile.write(payload)

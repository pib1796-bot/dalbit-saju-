# 달빛사주 Vercel 테스트 배포

Vercel에 이 폴더의 파일 전체를 배포합니다. API 키를 HTML이나 채팅에 붙여넣지 마세요.

프로젝트 Settings > Environment Variables에서 다음을 설정하세요:
- OPENAI_API_KEY: OpenAI 비밀키
- DALBIT_ACCESS_CODE: 임의의 긴 테스트용 접속 코드 (API 키와 다른 값)
- OPENAI_MODEL: gpt-4.1-mini (선택)

설정 후 Redeploy하세요. 사주 해설 화면의 접속 코드 칸에 DALBIT_ACCESS_CODE를 입력해야 요청할 수 있습니다. 코드가 공개되면 누구나 API 비용을 발생시킬 수 있으므로 지인에게만 공유하세요. 공개 상용 운영에는 사용자 인증, 서버측 호출 제한, 결제 및 실제 만세력 엔진 검증이 추가로 필요합니다.

**주의**: 현재 API는 검증된 사주팔자 계산이 없는 일반 명리학 해설 체험판입니다. 실제 개인 사주 풀이로 판매하면 안 됩니다. Vercel Hobby는 비상업용 테스트에만 사용하세요.

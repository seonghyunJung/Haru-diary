FROM nginx:1.22.0-alpine
# 실행이 되면 nginx의 기본 설정파일들을 없앤다.
RUN rm /etc/nginx/conf.d/default.conf
# 없앤 기본 설정파일들 대신 내가 만든 nginx.conf를 복사해 넣어준다.
COPY nginx.conf /etc/nginx/conf.d
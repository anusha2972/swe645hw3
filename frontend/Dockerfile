# Team members:
# 1. Anusha Gurram – G01514835
# 2. Bala Naga Tirumala Kiran Annadata – G01508483
# 3. Yashwanth Karthikeya Settem – G01512992

# Creates the Docker image for the React frontend and serves it with Nginx.

FROM node:20-alpine AS builder
WORKDIR /app


ARG VITE_API_BASE_URL=http://localhost:8000/api
ARG VITE_API_TIMEOUT_MS=15000
ENV VITE_API_BASE_URL=${VITE_API_BASE_URL}
ENV VITE_API_TIMEOUT_MS=${VITE_API_TIMEOUT_MS}

COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:1.27-alpine AS runtime
RUN apk --no-cache add curl


COPY nginx.conf /etc/nginx/conf.d/default.conf


COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -fsS http://127.0.0.1/healthz || exit 1

CMD ["nginx", "-g", "daemon off;"]

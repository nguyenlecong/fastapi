# fastapi
FastAPI learning[^1]

- [Khái niệm](#khai-niem)
- [Cài đặt](#cai-dat)
- [FastAPI docs](#fastapi-docs)
- [Create a simple APT](#create-api)
- [Path Parameters](#path-params)
- [Query parameters](#query-params)
- [Request Body](#req-body)
- [Query Parameters and String Validations](#string-valid)
- [Path Parameters and Numeric Validations](#numeric-valid)
- [Body](#body)
- [Security](#security)
***
- <a name="khai-niem">**Khái niệm:**</a>
  - >FastAPI framework, high performance, easy to learn, fast to code, ready for production
  - FastAPI là 1 web framework dùng để build API có hiệu năng cao, code đơn giản, hỗ trợ tốt cho việc làm sản phẩm
  - **Đặc điểm:**
    - **Fast:** Hiệu suất cao ngang với Nodejs và Go
    - **Fast to code:** Code nhanh hơn, tốc độ code các features tăng khoảng 200 đến 300%
    - **Fewer bugs:** giảm số bugs của dev đến 40%
    - **Intuitive:**  hỗ trợ code dễ hơn với tự động gợi ý, debug cầm ít thời gian hơn so với trước
    - **Easy:** dễ dùng, dễ đọc
    - **Short:** Tối thiểu lặp code. Các tham số truyền vào có nhiều tính năng. Ít bugs
    - **Robust:** hiệu năng mạnh mẽ, có thể tương tác API qua docs
    
- <a name="cai-dat">**Cài đặt:**</a>
  - Python 3.6+
  - fastapi: `pip install fastapi ([all])`
  - ASGI server khi deploy (uvicorn/hypercorn): `pip install uvicorn`
    - ASGI kết thừa từ WSGI
    - WSGI là 1 chuẩn giao tiếp giữa web server và Python app server; linh hoạt, xử lý nhiều request cùng lúc...
      
- <a name="fastapi-docs">**FastAPI Docs:**</a>
  - `http://0.0.0.0:8000/docs`
  - `http://0.0.0.0:8000/redoc`
    
- <a name="create-api">**Create a simple API:**</a>
  - Run app: `(python -m) uvicorn main:app --host 0.0.0.0 --port 8000 (--reload)` or `python run.py`
  - Check result: `http://127.0.0.1:8000`
    
- <a name="path-params">**Path Parameters:**</a>
  - Truyền parameter thông qua đường dẫn
  - Path parameters with types, data validation
  - FastAPI hỗ trợ khai báo đường dẫn trong đường dẫn
    
- <a name="query-params">**Query parameters:**</a>
  - Truyền dưới dạng key-value `http://127.0.0.1:8000/dbitems/?skip=0&limit=10`
  - Optional parameters: Có tác dụng check lỗi nếu xảy ra `http://127.0.0.1:8000/items/1?q=1  # 1 là item_id và ?q=1 là giá trị của q`
  - Query parameter type conversion: Thay đổi giá trị mặc định bằng cách truyền giá trị trên đường dẫn `http://127.0.0.1:8000/items/foo?short=1 or http://127.0.0.1:8000/items/foo?short=True`
  - Multiple path and query parameters: Với các đường dẫn lồng nhau, FastAPI biết param nào với param nào dựa trên tên param
  - Required query parameters: Thiếu param trên đường dẫn sẽ báo lỗi
    
- <a name="req-body">**Request Body:**</a>
  - Request body: người dùng gửi request từ browser đến API
  - Response body: dựa trên request, API trả về response cho người dùng
  - Pydantic Models
  - Use model
  - Request body + path parameters:
    - FastAPI hỗ trợ khai báo tham số URL và request body cùng lúc, framework sẽ biết tham số nào truyền từ đường dẫn và tham số nào lấy từ request
    - Tương tự, có thể thêm tham số URL, tham số query và request body cùng lúc
      
- <a name="string-valid">**Query Parameters and String Validations:**</a>
  - Attribute Optional có độ dài bị giới hạn không vượt quá 50 ký tự. Nên FastAPI cung cấp class Query
  - Query parameter list / multiple values: Ngoài định dạng string và integer, FastAPI còn hỗ trợ type List `http://localhost:8000/items/1/?q=foo&q=bar`
    
- <a name="numeric-valid">**Path Parameters and Numeric Validations:**</a>
  - Tương tự Query, FastAPI cung cấp class Path
  - Number validations
    
- <a name="body">**Body:**</a>
   - Multiple Parameters: FastAPI hỗ trợ tạo format cho request body
   - Singular values in body: có thể thêm define 1 body cho chỉ 1 giá trị mà không cần khai báo class
   - Multiple body params and query: đơn giản là kết hợp multiple body param với query param
   - Field: validate data hoặc thêm metadata trong 1 class
   - Nested Models: Ngoài các kiểu int, float, str, có thể thêm kiểu list hay set
     
- <a name="security">**Security:**</a>
  - Do based trên OpenAPI nên FastAPI thừa kế security flow của OpenAPI
  - apiKey: chỉ là key mà thôi, có thể đến từ query param, header hoặc cookie.
  - http: hệ thống xác thực của HTTP, bao gồm:
    - bearer: header param với giá trị là một token (thừa kế từ OAuth2)
    - HTTP Basic authentication
    - HTTP Digest authentication
  - oauth2: Là 1 chuẩn giao thức ủy quyền ra đời vào tháng 10 năm 2012, được sử dụng ở hầu hết mọi ứng dụng (web, mobile), cho phép người dùng cung cấp thông tin cá nhân bởi ứng dụng của bên thứ 3, cũng được dùng để cung cấp cơ chế cho việc xác thực người dùng
  - openIdConnect: Based trên OAuth2, là 1 layer nằm phía trên giao thức OAuth2
  - OAuth2 với Password và Bearer
  - Get current user
  - OAuth2 với Password (có hashing), Bearer với JWT tokens:
    - JWT, viết tắt của JSON Web Tokens, là 1 chuỗi các ký tự, dạng mã hóa của Json
    - Các thư viện cần cài thêm: jose (để sinh JWT token, passlib (hash password))
      - `pip install python-jose[cryptography]`
      - `pip install passlib[bcrypt]`

[^1]: [Hướng dẫn cơ bản framework FastAPI từ A -> Z](https://viblo.asia/p/huong-dan-co-ban-framework-fastapi-tu-a-z-phan-1-V3m5W0oyKO7)

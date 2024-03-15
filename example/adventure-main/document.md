#  API Document
Tài liệu được viết để các thành viên nắm bắt được cách sử dụng các thành phần có sẵn trong tầng framework.

## Assets
Các assets được tổ chức ở tầng cùng tên, bao gồm các thư mục con : `animation, texture, font, audio, ...` tương ứng. Trong đó cần lưu ý cách tổ chức:
- Các assets của **animation** được đặt trong thư mục có **tên là tên của animation**, đánh số các **frame** từ 0 -> hết. 
Ví dụ: thư mục "idle" chứa các ảnh 0.png, 1.png, 2.png, 3. png
- Ngay sau khi thêm assets, cần chạy file **__gen__.py** để sinh ra các file python tương ứng.
- Các assets khác được đặt trong thư mục tương ứng, có thể đặt tên tùy ý nhưng cần đảm bảo không trùng với tên của các assets khác và không chứa ký tự đặc biệt ngoại trừ dấu underscore.

![assets_struct](https://media.discordapp.net/attachments/960780341952544798/1161998326082838628/image.png?ex=653a5645&is=6527e145&hm=2ef4758a1329d086f7321600a991c59cdd281c3c74ee96c81d30872f2e2b591d&=&width=332&height=621)
## State
Trong dự án, chúng ta coi mỗi màn hình là một State, các lớp kế thừa **BaseState** đều được cung cấp tất cả mọi thứ để khởi tạo một màn hình.  <br>
Có thể quản lý các màn hình bằng **StateMachine** (push, pop)
## Entity
Các entity là các thực thể ở trong màn hình play của game, bao gồm các nhân vật, khối gạch, đạn, ... 
Có 2 cách vẽ entity: 
- Sử dụng hệ thống animation với **Animation Manager**
	```python
	self.animation_manager = AnimationManager(
	        action_animation = {
	            'roll': ActionAnimation(Assets.roll, 5, self, delay=2),
	            'test': ActionAnimation(Assets.test, 10, self, delay=2),
	        },
	        repeat_animation = {
	            'walk': RepeatAnimation(Assets.walk, 8, self, delay=2),
	            'idle': RepeatAnimation(Assets.idle, 6, self, delay=2),
	            'test2': RepeatAnimation(Assets.test2, 10, self, delay=2),
	        },
	        current_animation = 'idle'
	    )
	```
	Trong đó tham số thứ 3 phải là tên một RepeatAnimation đại diện cho trạng thái khởi tạo của nhân vật.

- Sử dụng hệ thống Texture:
	```python
	self.texture = Texture(texture=texture, entity=self)
	```

## Widget
Là các thành phần trong các màn hình như menu, settings, ... bao gồm các button, text, ... 

## Localization
Là hệ thống dịch ngôn ngữ, được sử dụng để dịch các text trong game sang các ngôn ngữ khác nhau.
- Các ngôn ngữ được định nghĩa trong folder **strings** với đuôi là **.json**.
- Các text được định nghĩa trong các file json tương ứng, với key là tên của text, value là nội dung của text.
- Sau khi thêm hoặc sửa các file json, chạy file **__gen__.py** để sinh ra các file python tương ứng.
- Sử dụng:
	'''python
	from framework.framework import Localization as S
	text = S().key # get text with key
	S.language = 'vi' # change locale
	'''


Sample code: [Sample code](example.md)
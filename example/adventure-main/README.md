# BTL-Python-2023
Project bài tập lớn môn Python kỳ 1 năm 3, năm học 2023 - 2024.

Giảng viên: Nguyễn Trọng Khánh

Nhóm: 09

Nhóm bài tập: 06

## Tech stack
- Python
- Pygame

## Conventions
- Commit: `[Py-06] commit name`
- Branch: `feature/Py-06-branch-name`, `bugfix/Py-06-branch-name`, `hotfix/Py-06-branch-name`
- PR title: `Py-06: Your title`

## Gitflow
### Được giao task mới
- Pull develop: `git pull origin develop`
- Tạo nhánh mới từ develop: `git checkout -b <tên-branch>`
- Code x3,14
### Đang làm task cũ
- Pull develop về nhánh hiện tại vào mỗi ngày làm việc mới: `git pull origin develop`
- Code x3,14
- Commit và push code lên github mỗi khi kết thúc ngày làm việc:
  - `git add.`
  - `git commit -m "Message"`
  - `git push origin <tên-branch-hiện-tại>`

## Một vài câu lệnh git
- `git clone <url>`: clone repository về máy
- `git add .`: add toàn bộ thay đổi để commit
- `git commit -m "Commit Message"`: commit toàn bộ thay đổi với message chỉ định vào nhánh hiện tại
- `git push origin <tên-branch>`: push toàn bộ commit (tức là sự thay đổi về các file) ở nhánh hiện tại lên nhánh được chỉ định trên github
- `git pull origin <tên-branch>`: lấy toàn bộ commit (tức là sự thay đổi về các file) ở nhánh được chỉ định từ github về nhánh hiện tại
- `git checkout <tên-branch>`: chuyển sang nhánh được chỉ định
- `git checkout -b <tên-branch>`: tạo branch mới và chuyển sang đó (tên branch không được trùng nhau)
- `git branch -d <tên-branch>`: xoá branch được chỉ định khỏi máy (đương nhiên toàn bộ thay đổi có ở nhánh này cũng sẽ mất hết)
- **Nếu không quen có thể sử dụng GUI của VSC**

## Documents
- Để hiểu hơn về project và các coding convention trong project, vui lòng đọc [tài liệu](document.md) được biên soạn bởi Cao Việt Đức

# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from GeezProject.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL, OWNER
class Messages():
      HELP_MSG = [
        ".",
f"""
**Chào mừng bạn quay trở lại {PROJECT_NAME}

✣️ {PROJECT_NAME} có thể Phát các bài hát trong Trò chuyện bằng giọng nói Nhóm một cách dễ dàng.

✣️ Trợ lý âm nhạc » @{ASSISTANT_NAME}\n\nNhấp vào Tiếp theo để xem hướng dẫn**

""",

f"""
**Sắp xếp**

1. Đặt bot làm quản trị viên
2. Bắt đầu trò chuyện thoại / VCG
3. Gõ `/userbotjoin` và thử /play <tên bài hát>
× Nếu Assistant Bot tham gia thưởng thức âm nhạc,
× Nếu Trợ lý Bot không tham gia Vui lòng thêm @{ASSISTANT_NAME} vào nhóm của bạn và thử lại


**» Đặt hàng cho các thành viên trong nhóm cũng có thể :**

 × /playlist : Để hiển thị danh sách Bài hát hiện tại
 × /current : Hiển thị bài hát hiện tại đang phát
 × /song <tên bài hát> : Để tải xuống các bài hát trên YouTube
 × /video <tên bài hát> : Để tải xuống video trên YouTube với thông tin chi tiết
 × /vsong <tên bài hát> : Để tải xuống video trên YouTube với thông tin chi tiết
 × /deezer <tên bài hát> : Để tải xuống các bài hát từ deezer
 × /saavn <tên bài hát> : Để tải xuống các bài hát từ trang web saavn
 × /search <tên bài hát> : Để tìm kiếm video trên YouTube với thông tin chi tiết

**» Lệnh Chỉ dành cho Quản trị viên :**

× /play <tên bài hát> : Để phát bài hát bạn yêu cầu qua youtube
× /play <link yt> : Để phát bài hát bạn yêu cầu qua liên kết youtube
× /play <trả lời âm thanh> : Để phát bài hát bạn yêu cầu qua tệp âm thanh
× /dplay : Để phát bài hát bạn yêu cầu qua deezer
× /splay : Để phát bài hát bạn yêu cầu qua jio saavn
× /skip : Để Bỏ qua việc phát lại bài hát sang Bài hát tiếp theo
× /pause : Để tạm dừng phát lại bài hát
× /resume : Để tiếp tục phát lại bài hát bị tạm dừng
× /end : Để dừng phát lại bài hát
× /userbotjoin - Để mời trợ lý vào cuộc trò chuyện của bạn
× /admincache - Để làm mới danh sách quản trị viên
"""
      ]

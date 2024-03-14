from ..core.singleton import Singleton
class Localization(Singleton):
    language = 'en'
    languages = set()
    strings = dict()
    languages = {'vi', 'en'}
    strings = {
        'en': {
            'all_settings': 'Setting', 
            'all_back': 'Back', 
            'all_continue': 'Continue', 
            'all_restart': 'Restart', 
            'all_menu': 'Home', 
            'all_start': 'Start', 
            'all_about': 'About', 
            'setting_audio_toggle': 'Audio Effects', 
            'setting_music_toggle': 'Music', 
            'setting_language': 'Language', 
            'setting_language_en': 'English', 
            'setting_language_vi': 'Vietnamese', 
            'loose_gameover': 'Game over!', 
            'get_key': 'You got a key!', 
            'hint_message': 'Follow the ground to find the key', 
            'all_author': 'AUTHOR: ',
            'all_author_name': 'Cao Viet Duc\nNguyen Hoang Dang\nLuu Ngoc Anh\nNguyen Duc Loc\nNguyen Tat Binh',
            'all_game': 'GAME INSTRUCTIONS: ',
            'all_game_instructions': 
                '''
                ->  You are stuck in an infinite loop. To escape the loop, you need to find the chest
                containing the key in the well mouth area. Of course, normally the chest will be 
                hidden.
                ->  When you have not found the key and go to the 2 exits on the right and bottom 
                of the screen, the level will be reset and you will have to start from the beginning.
                ->  The player's task is to find the moving code to make the well light up. The 
                password hint will be hidden somewhere in objects on the map. Press "f" to open 
                hints.
                ->  On the way, you will also encounter many monsters blocking your way. Use 
                the arrow keys on the keyboard to move and the "SPACE" key to attack monsters, 
                defeat them and continue searching.
                ->  When the mouth of the well lights up, the hidden chest will appear. Press "f" 
                to open the chest and get the key to exit the loop.
                Good luck!
                ''',
            'win_message_1': 'Victory',
            'win_message_2': 'Congratulations, you have escaped the loop!!!'    
        },
        'vi': {
            'all_settings': 'Cài đặt', 
            'all_back': 'Quay lại', 
            'all_continue': 'Tiếp tục', 
            'all_restart': 'Chơi lại', 
            'all_menu': 'Trang chủ', 
            'all_start': 'Bắt đầu', 
            'all_about': 'Giới thiệu', 
            'setting_audio_toggle': 'Hiệu ứng âm thanh', 
            'setting_music_toggle': 'Âm nhạc', 
            'setting_language': 'Ngôn ngữ', 
            'setting_language_en': 'Tiếng Anh', 
            'setting_language_vi': 'Tiếng Việt', 
            'loose_gameover': 'Trò chơi kết thúc!', 
            'get_key': 'Bạn đã nhận được chìa khóa!', 
            'hint_message': 'Nhìn vào mặt đất để tìm chìa khóa',
            'all_author': 'TÁC GIẢ: ',
            'all_author_name': 'Cao Việt Đức\nNguyễn Hoàng Đăng\nLưu Ngọc Anh\nNguyễn Đức Lộc\nNguyễn Tất Bình',
            'all_game': 'HƯỚNG DẪN CHƠI: ',
            'all_game_instructions':
                '''
                ->  Bạn bị mắc kẹt trong một vòng lăp vô hạn. Để thoát khỏi vòng lặp, bạn cần phải 
                tìm được chiếc rương chứa chìa khóa ở khu vực miệng giếng. Tất nhiên bình thường 
                chiếc rương sẽ bị ẩn đi. 
                ->  Khi bạn chưa tìm được chìa khóa mà đi đến 2 lối ra ở bên phải và phía dưới màn
                hình, màn chơi sẽ được reset và bạn sẽ phải bắt đầu lại từ đầu. 
                ->  Nhiệm vụ của người chơi là phải tìm mật mã di chuyển cho chiếc giếng sáng lên. 
                Gợi ý của mật mã sẽ được giấu đâu đó trong các vật thể trên bản đồ. Ấn "f" để mở 
                gợi ý. 
                ->  Trên đường đi, bạn cũng sẽ gặp rất nhiều quái vật cản đường. Sử dụng PHÍM MŨI 
                TÊN trên bàn phím để di chuyển và phím "SPACE" để tấn công quái vật, đánh bại 
                chúng và tiếp tục tìm kiếm. 
                ->  Khi miệng giếng sáng lên, chiếc rương bị ẩn sẽ hiện ra. Ấn "f" để mở rương và 
                lấy chìa khóa thoát khỏi vòng lặp. 
                Chúc bạn may mắn!
                ''',
            'win_message_1': 'Chiến thắng', 
            'win_message_2': 'Chúc mừng bạn đã thoát khỏi vòng lặp!!!'           
            }
    }

    @property
    def all_settings(self):
        return Localization.strings[Localization.language]['all_settings']
    
    @property
    def all_back(self):
        return Localization.strings[Localization.language]['all_back']
    
    @property
    def all_continue(self):
        return Localization.strings[Localization.language]['all_continue']
    
    @property
    def all_restart(self):
        return Localization.strings[Localization.language]['all_restart']
    
    @property
    def all_menu(self):
        return Localization.strings[Localization.language]['all_menu']
    
    @property
    def all_start(self):
        return Localization.strings[Localization.language]['all_start']
    
    @property
    def all_about(self):
        return Localization.strings[Localization.language]['all_about']
    
    @property
    def setting_audio_toggle(self):
        return Localization.strings[Localization.language]['setting_audio_toggle']
    
    @property
    def setting_music_toggle(self):
        return Localization.strings[Localization.language]['setting_music_toggle']
    
    @property
    def setting_language(self):
        return Localization.strings[Localization.language]['setting_language']
    
    @property
    def setting_language_en(self):
        return Localization.strings[Localization.language]['setting_language_en']
    
    @property
    def setting_language_vi(self):
        return Localization.strings[Localization.language]['setting_language_vi']
    
    @property
    def loose_gameover(self):
        return Localization.strings[Localization.language]['loose_gameover']
    
    @property
    def get_key(self):
        return Localization.strings[Localization.language]['get_key']
    
    @property
    def hint_message(self):
        return Localization.strings[Localization.language]['hint_message']
    @property
    def all_author(self):
        return Localization.strings[Localization.language]['all_author']
    @property
    def all_author_name(self):
        return Localization.strings[Localization.language]['all_author_name']
    @property
    def all_game(self):
        return Localization.strings[Localization.language]['all_game']
    @property
    def all_game_instructions(self):
        return Localization.strings[Localization.language]['all_game_instructions']
    @property
    def win_message_1(self):
        return Localization.strings[Localization.language]['win_message_1']
    @property
    def win_message_2(self):
        return Localization.strings[Localization.language]['win_message_2']
    
    
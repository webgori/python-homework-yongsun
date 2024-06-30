class Song():
    def set_song(self, name, genre):
        self.name = name
        self.genre = genre

    def print_song(self):
        print(f'노래 제목: {self.name}({self.genre})')


class Singer():
    def set_singer(self, singer):
        self.singer = singer

    def hit_song(self, song):
        self.hit_song = song
    
    def print_singer(self):
        print(f'가수 이름: {self.singer}')
        print(f'노래 제목: {self.hit_song.name}({self.hit_song.genre})')



song = Song()
song.set_song('취중진담', '발라드')

singer = Singer()
singer.set_singer('김동률')

singer.hit_song(song)

singer.print_singer()
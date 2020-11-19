class Track:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'{self.name}-{self.duration}'

    def __lt__(self, other):
        if not isinstance(other, Track):
            return 'Other not a track'
        else:
            return self.duration < other.duration


class Album:

    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.tracks = []

    def get_tracks(self):
        for track in self.tracks:
            print(track)

    def add_track(self, track):
        self.tracks.append(track)

    def get_duration(self):
        full_duration = 0

        for track in self.tracks:
            full_duration += track.duration

        print(f'Full duration {self.name}: {full_duration}')

    def __info(self):
        print(f'Name group: {self.artist}\nName album: {self.name}\nTracks:')

        for track in self.tracks:
            print(f'\t\t{track}min')

        return ''

    def __str__(self):
        return str(self.__info())


def place_tracks(album, tracks):
    for track in tracks:
        album.add_track(track)

def main():

    album_scratchpaper = Album('ScratchPaper', 'Fukkit')

    track_flashbang = Track('FlashBang', 2)
    track_woke = Track('Woke', 2)
    track_mincemeat = Track('Mincemeat', 1)

    scratchpaper_tracks = [track_flashbang, track_woke, track_mincemeat]

    album_snowball = Album('Snowball', 'Heartsnow')

    track_onetouch = Track('Одно касание', 2)
    track_darkcases = Track('Темные дела', 3)
    track_shift = Track('Shift', 1)

    snowball_tracks = [track_onetouch, track_darkcases, track_shift]

    place_tracks(album_scratchpaper, scratchpaper_tracks)
    place_tracks(album_snowball, snowball_tracks)

    print(album_scratchpaper)
    print(album_snowball)

    print(track_shift > track_onetouch)
    print(track_mincemeat < track_flashbang)


if __name__ == '__main__':
    main()

from data_structures import TwoWayNodeQueue
from time import sleep



class MusicPlayer(TwoWayNodeQueue):
    
    def play_all(self):
        if self.front is not None:
            current_song = self.front

            while current_song is not None:
                print('Reproducing... ', current_song.data)
                
                current_song = current_song.previous

                sleep(1.5)


if __name__ == '__main__':
    mp3 = MusicPlayer()

    mp3.add('Beliver - Imagine Dragons')
    mp3.add('Beggin - Maneskin')
    mp3.add('Jhonny B. Goode - Berry Is On Top')

    mp3.play_all()

    mp3.pop()
    print('\n\n', 'After pop function.\n')

    mp3.play_all()

    

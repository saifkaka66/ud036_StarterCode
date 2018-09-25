import media
import fresh_tomatoes


'''choosing favorite movies and providing their titles,
   posters and trailer videos
'''

inception = media.Movie('inception',
                        r'https://upload.wikimedia.org/wikipedia/en/2/2e/Ince'
                        'ption_%282010%29_theatrical_poster.jpg',
                        r'https://www.youtube.com/watch?v=d3A3-zSOBT4&feature'
                        '=youtu.be')

wonder_woman = media.Movie('wonder woman',
                           r'https://upload.wikimedia.org/wikipedia/en/e/ed/W'
                           'onder_Woman_%282017_film%29.jpg',
                           r'https://youtu.be/VSB4wGIdDwo')

baby_driver = media.Movie('baby driver',
                          r'https://upload.wikimedia.org/wikipedia/en/8/8e/Ba'
                          'by_Driver_poster.jpg',
                          r'https://youtu.be/z2z857RSfhk')

the_big_sick = media.Movie('the big sick',
                           r'https://upload.wikimedia.org/wikipedia/en/6/69/T'
                           'he_Big_Sick.jpg',
                           r'https://youtu.be/cLM5DdUhkoM')

john_wick_Chapter_two = media.Movie('john wick: chapter 2',
                                    r'https://upload.wikimedia.org/wikipedia/'
                                    'en/3/31/John_Wick_Chapter_Two.png',
                                    r'https://youtu.be/zZdMFH3GtIA')

atomic_blonde = media.Movie('atomic blonde',
                            r'https://upload.wikimedia.org/wikipedia/en/b/b5/'
                            'Atomic_Blonde_poster.jpg',
                            r'https://youtu.be/P00h-miJoRI')


'''listing all the movie names to be accessible to 'fresh_tomatoes' module
and finally appear in an '.html' file
'''
movies = [inception, wonder_woman, baby_driver,
          the_big_sick, john_wick_Chapter_two, atomic_blonde]

fresh_tomatoes.open_movies_page(movies)

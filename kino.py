from kinopoisk.movie import Movie


def find_movie(text):
    movie_list = Movie.objects.search(text)
    return None if len(movie_list) == 0 else {'id': movie_list[0].id,
                                              'title': movie_list[0].title,
                                              'title_en': movie_list[0].title_en,
                                              'year': movie_list[0].year,
                                              'rating': movie_list[0].rating,
                                              'url': f'https://www.kinopoisk.ru/series/{movie_list[0].id}' if
                                              movie_list[
                                                  0].series is True else f'https://www.kinopoisk.ru/film/{movie_list[0].id}'
                                              }

# test = find_movie('Вий')
# test1 = find_movie('Триггер')
# print(test, test1)

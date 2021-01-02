from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def entry_level_1():
    return data_manager.execute_select("""SELECT shows.title, COUNT(e.id) AS episodes
                                            FROM shows
                                            JOIN seasons ON seasons.show_id = shows.id
                                            JOIN episodes e ON seasons.id = e.season_id
                                            GROUP BY shows.title
                                            ORDER BY shows.title ASC;""")


def entry_level_2():
    return data_manager.execute_select(""" SELECT actors.name, COUNT(DISTINCT sc.character_name) AS counts, 
                                            string_agg(DISTINCT sc.character_name::text, ', ')
                                            FROM actors
                                            JOIN show_characters sc ON actors.id = sc.actor_id
                                            GROUP BY actors.name
                                            ORDER BY counts DESC LIMIT 10;""")


def entry_level_3(season_num, episode_num):
    return data_manager.execute_select("""SELECT shows.title AS shows
                                            FROM shows
                                            JOIN seasons s ON shows.id = s.show_id
                                            JOIN episodes e ON s.id = e.season_id
                                            JOIN show_genres sg ON shows.id = sg.show_id
                                            JOIN genres g ON g.id = sg.genre_id
                                            GROUP BY shows.title
                                            HAVING COUNT( DISTINCT s.season_number) >= %(season_num)s
                                            AND COUNT(e.episode_number) >= %(episode_num)s;""",
                                       {'season_num': season_num, 'episode_num': episode_num})


def pa_1(genre):
    return data_manager.execute_select("""SELECT shows.title, shows.year, ROUND(shows.rating)::INTEGER AS rating
                                            FROM shows
                                            JOIN show_genres sg ON shows.id = sg.show_id
                                            JOIN genres g ON g.id = sg.genre_id
                                            WHERE g.name = %(genre)s
                                            GROUP BY shows.title, shows.year, shows.rating
                                            ORDER BY shows.rating DESC LIMIT 10;""",
                                       {'genre': genre})

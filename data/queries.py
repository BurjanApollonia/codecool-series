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


def pa_2():
    return data_manager.execute_select("""SELECT CAST(EXTRACT(YEAR FROM shows.year) AS INTEGER ) AS year, COUNT(shows.title) AS counts, 
                                            ROUND(AVG(shows.rating), 1) AS rating
                                            FROM shows
                                            WHERE CAST(EXTRACT(YEAR FROM shows.year) AS INTEGER ) BETWEEN '1970' AND '2010'
                                            GROUP BY shows.year
                                            ORDER BY shows.year;""")


def pa_3():
    return data_manager.execute_select("""SELECT shows.title AS title
                                            FROM shows
                                            JOIN seasons s ON shows.id = s.show_id
                                            JOIN episodes e ON s.id = e.season_id
                                            GROUP BY shows.title, shows.runtime
                                            ORDER BY  COUNT(episode_number) * shows.runtime DESC LIMIT 10;""")


def pa_3_2(title):
    return data_manager.execute_select("""SELECT actors.name
                                            FROM actors
                                            JOIN show_characters sc on actors.id = sc.actor_id
                                            JOIN shows s on s.id = sc.show_id
                                            WHERE s.title = %(title)s;""",
                                       {'title': title})


def pa_9(search):
    return data_manager.execute_select("""SELECT shows.title AS title, sc.character_name AS charactername, 
                                            a.name AS actorname
                                            FROM shows
                                            INNER JOIN show_characters sc ON shows.id = sc.show_id
                                            INNER JOIN actors a ON a.id = sc.actor_id
                                            WHERE shows.title ILIKE %(search)s
                                            OR sc.character_name ILIKE %(search)s 
                                            OR a.name ILIKE %(search)s;""",
                                       {'search': search})


def pa_11():
    return data_manager.execute_select("""SELECT genres.name AS name, genres.id AS id
                                            FROM genres;""")


def pa_11_2(id_s):
    return data_manager.execute_select("""SELECT shows.id, shows.title AS title, COUNT(DISTINCT s.id) AS season_number, 
                                            COUNT(DISTINCT e.id) AS episode_number
                                            FROM shows
                                            JOIN seasons s ON shows.id = s.show_id
                                            JOIN episodes e ON s.id = e.season_id
                                            JOIN show_genres sg ON shows.id = sg.show_id
                                            JOIN genres g ON g.id = sg.genre_id
                                            WHERE g.id = %(id_s)s
                                            GROUP BY shows.id
                                            HAVING COUNT(e.episode_number) > 19
                                            ORDER BY COUNT(e.episode_number) DESC
                                            LIMIT 50;""",
                                       {'id_s': id_s})

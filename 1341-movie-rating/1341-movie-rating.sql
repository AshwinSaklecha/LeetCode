# Write your MySQL query statement below
(select u.name as results from MovieRating mr
left join Users u on mr.user_id = u.user_id
left join Movies m on mr.movie_id = m.movie_id
group by mr.user_id
order by -count(mr.rating), u.name
limit 1)

union all

(select m.title as results from MovieRating mr
left join Users u on mr.user_id = u.user_id
left join Movies m on mr.movie_id = m.movie_id
where year(mr.created_at) = 2020 and month(mr.created_at) = 02
group by m.title
order by -avg(mr.rating), m.title
limit 1)
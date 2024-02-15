-- 코드를 입력하세요
SELECT member_id, member_name, gender, date_format(date_of_birth, '%Y-%m-%d') as birth
from member_profile
where gender = 'W' and tlno is not null and substring(date_of_birth, 6, 2) = '03'
order by member_id asc
;
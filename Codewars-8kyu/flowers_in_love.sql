SELECT flower1, flower2,
CASE
       WHEN flower1 % 2 = 0 AND flower2 % 2 = 0 THEN False
       WHEN flower1 % 2 !=0 AND flower2 % 2 !=0 THEN False
       ELSE True
       END
       AS res
FROM love
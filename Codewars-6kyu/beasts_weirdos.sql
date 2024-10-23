SELECT th.id, th.heads, bh.legs, th.arms, bh.tails,
  CASE
    WHEN th.heads > th.arms OR bh.tails > bh.legs THEN 'BEAST'
    ELSE 'WEIRDO'
  END AS species
FROM top_half th
JOIN bottom_half bh ON bh.id = th.id
ORDER BY species
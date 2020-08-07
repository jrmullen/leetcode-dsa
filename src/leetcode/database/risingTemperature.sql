-- MySQL

SELECT w1.Id
from Weather w1,
     Weather w2
WHERE w1.Temperature > w2.Temperature
  AND DATEDIFF(w1.RecordDate, w2.RecordDate) = 1;
  
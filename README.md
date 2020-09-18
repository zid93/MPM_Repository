# MPM_Repository

select * from (
select pen.Nama, tanggalPisah, ROW_NUMBER () OVER (ORDER BY tanggalPisah desc) as "tanggalPisahID"  
from pasangan p inner join perpisahan pe on (p.ID = pe.PasanganID)
inner join penduduk pen on (p.pendudukid = pen.id)
) x limit 100

or 

select pen.Nama, tanggalPisah as "tanggalPisah"
from pasangan p inner join perpisahan pe on (p.ID = pe.PasanganID)
inner join penduduk pen on (p.pendudukid = pen.id)
order by p.id desc limit 100;

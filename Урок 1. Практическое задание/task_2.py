# я сделал 2 варианта задания, потому что пример выполнения задания я счел некорректным
seconds = int(input("input seconds: "))
# 1 вариант - согласно примеру
print(f"time in the format hh:mm:ss - {seconds/3600:.1f} : {seconds/60:.1f} : {seconds}")
# 2 вариант - согласно моему пониманию
hours = seconds // 3600
seconds -= hours * 3600
minutes = seconds // 60
seconds -= minutes * 60
print(f"time in the format hh:mm:ss - {hours:02} : {minutes:02} : {seconds:02}")

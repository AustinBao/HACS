total_scoville = 0

all_peppers = {"Poblano":1500,"Mirasol":6000,"Serrano":15500,"Cayenne":40000,"Thai":75000, "Habanero":125000}

num_of_peppers = int(input())
for i in range(num_of_peppers):
    peppers = input()
    total_scoville += all_peppers[peppers]

print(total_scoville)
    


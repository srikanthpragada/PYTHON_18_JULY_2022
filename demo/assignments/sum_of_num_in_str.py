st = "10,20,30,av,40"

nums = st.split(",")
vnums = filter(str.isdigit, nums)
print(sum(map(int, vnums)))

print(sum([int(n) for n in st.split(",") if n.isdigit()]))

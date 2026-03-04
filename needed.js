student={
    name:'Yuvraj',
    age:23,
    marks:
    {"science":29,"maths":45,"phy":65,"social":43}
}
console.log(student.name)
console.log(student.age)
console.log(student.marks['science']);
let total=0
let count=0
for(let i in student.marks){
total+=student.marks[i]
count++
}
print(total/4)
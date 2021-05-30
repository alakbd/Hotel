

//user name validation starts
function username_validation(){
        //'use strict';
        var username_name = document.getElementById("username");
        var username_value = document.getElementById("username").value;
        var username_length = username_value.length;
        var letters = /^[A-Za-z ]+$/;
        if(username_length < 4 || !username_value.match(letters))
        {
        document.getElementById('name_err').innerHTML = 'Name must be more than letters.';
        
        document.getElementById('name_err').style.color = "#FF0000";
        }
        else
        {
        document.getElementById('name_err').innerHTML = 'Valid Name';
        document.getElementById('name_err').style.color = "#00AF33";
        }
}

//user name validation ends

//address validation start
 function address_validation()
    {
     //'use strict';
        var address_name = document.getElementById("address");
        var address_value = document.getElementById("address").value;
        if(address_value == "")
        {
        document.getElementById('add_err').innerHTML = 'You must Enter Address.';
        
        document.getElementById('add_err').style.color = "#FF0000";
        }
        else
        {
        document.getElementById('add_err').innerHTML = 'Address entered';
        document.getElementById('add_err').style.color = "#00AF33";
        }
}
    //address validation start
//personal id validation start
function personaliDT_validation()
 {
    //'use strict';
        var country_name = document.getElementById("pdt");
        var country_value = document.getElementById("pdt").value;
        if(country_value === "Default" || country_value === "--")
        {
        document.getElementById('pdt_err').innerHTML = 'You must select a ID';
        
        document.getElementById('pdt_err').style.color = "#FF0000";
        }
        else
        {
        document.getElementById('pdt_err').innerHTML = 'ID selected.';
        document.getElementById('pdt_err').style.color = "#00AF33";
        }
}
function IDnumber_validation()
{
        //'use strict';
        var country_name = document.getElementById("IDnumber");
        var id_value = document.getElementById("IDnumber").value;
        if(id_value == "")
        {
        document.getElementById('IDnumber_err').innerHTML = 'You must Enter ID number';
        
        document.getElementById('IDnumber_err').style.color = "#FF0000";
        }
        else
        {
        document.getElementById('IDnumber_err').innerHTML = 'ID entered';
        document.getElementById('IDnumber_err').style.color = "#00AF33";
        }
}
    //personal id validation end
//country validation starts
function country_validation(){
//'use strict';
var country_name = document.getElementById("country");
var country_value = document.getElementById("country").value;
if(country_value === "Default" || country_value === "--")
{
    document.getElementById('country_err').innerHTML = 'You must select a country';

    document.getElementById('country_err').style.color = "#FF0000";
}
else
{
    document.getElementById('country_err').innerHTML = 'Country selected.';
    document.getElementById('country_err').style.color = "#00AF33";
}
}
//country validation ends
//phone validation
function phonenumber_validation()
{
    //'use strict';
    var phoneno = /^\+?([0-9]{2})\)?[-. ]?([0-9]{4})[-. ]?[0-9]+$/;
    var inputPhonename = document.getElementById("phone");
    var inputno = document.getElementById("phone").value;
    if(inputno.match(phoneno) )
        {
        document.getElementById('phone_err').innerHTML = 'Valid phone No.';
        document.getElementById('phone_err').style.color = "#00AF33";
        }
    else
        {
        document.getElementById('phone_err').innerHTML = 'You must enter a valid phone number.';
        
        document.getElementById('phone_err').style.color = "#FF0000";
        
        }
}
//zip validation starts
function zip_validation(){
    //'use strict';
    var numbers = /^[0-9]+$/;
    var zip_name = document.getElementById("zip");
    var zip_value = document.getElementById("zip").value;
    var zip_length = zip_value.length;
    if(!zip_value.match(numbers) || zip_length !== 5)
    {
    document.getElementById('zip_err').innerHTML = 'You must enter a ZIP code, which must be numeric and must be at least 5 chracters long.';
   
    document.getElementById('zip_err').style.color = "#FF0000";
    }
    else
    {
    document.getElementById('zip_err').innerHTML = 'ZIP code entered';
    document.getElementById('zip_err').style.color = "#00AF33";
    }
}
//zip validation ends
//email validation starts
function email_validation(){
//'use strict';
var mailformat = /^\w+([\.\-]?\w+)*@\w+([\.\-]?\w+)*(\.\w{2,3})+$/;
var email_name = document.getElementById("email");
var email_value = document.getElementById("email").value;
var email_length = email_value.length;
if(!email_value.match(mailformat) || email_length === 0)
{
document.getElementById('email_err').innerHTML = 'This is not a valid email format.';

document.getElementById('email_err').style.color = "#FF0000";
}
else
{
document.getElementById('email_err').innerHTML = 'Valid email format';
document.getElementById('email_err').style.color = "#00AF33";
}
}
//email validation ends
//gender validation starts
function gender_validation(){
//'use strict';
if ( (document.getElementById("msex").checked === false) && (document.getElementById("fsex").checked === false)){
document.getElementById('gender_err').innerHTML = 'Please slect a geneder.';
document.getElementById('gender_err').style.color = "#FF0000";
document.getElementById("msex").checked = true;
}
else
{
document.getElementById('gender_err').innerHTML = 'Gender selected';
document.getElementById('gender_err').style.color = "#00AF33";
}
}
//gender validation ends
//All field validation start
//function required() {

//    var uname = document.getElementById("username").value;
//    var inputno = document.getElementById("phone").value;
//    var addr = document.getElementById("address").value;;
//    if (uname == '')
//    {
//        alert("Please insert all the required fields");
//    }
//    else
      
//    {
//        alert("success");
//        //r c = "https://alak.dbsprojects.ie:8080/bookingDetailsEntry";
//        //window.location.href = "renderpage.html?uname=" + uname + "&inputno= " + inputno;


//    }
    
//    //if (inputno == '')
//    //    alert("Please insert all the required fields");
   
//    ////if (addr == '')
//    ////    alert("Please insert all the required fields");

//    //var e = document.getElementById("PersonalIDType");
//    //var idtype = e.options[e.selectedIndex].text;//get the selected option text

//    //var idnum = document.forms["registration"]["IDnumber"].value;

//    //var f = document.getElementById("country");
//    //var countryname = f.options[e.selectedIndex].text;//get the selected option text

//    //var zipname = document.forms["registration"]["zip"].value;
//    //var emailname = document.forms["registration"]["email"].value;

//    //var g = document.getElementById("gender");
//    //var gender = g.options[e.selectedIndex].text;//get the selected option text
//    //    //document.getElementById("msex").checked === false;

    
//}
    //all field validation end

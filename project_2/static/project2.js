const display=document.getElementById("50");

display.addEventListener("click" ,()=>{
    if(navigator.geolocation)
    {   display.innerText="click to get location";
       navigator.geolocation.getCurrentPosition(onsuccess,onerror);
    }
    else {
        display.innertext="your browser does not support geolocation services ";
    }

});

function onsuccess(position)
{      display.innerText="DETECTING YOUR LOACTION....";
    let{longitude,latitude}=position.coords;
    console.log(latitude,longitude);

 fetch('https://api.opencagedata.com/geocode/v1/json?q=latitude+longitude &key=50f98505d181400b9e23f4f8bc312141')
 .then(response=>response.json()).then (result => {
     let allDetails =  result.results[0].components;
     let {county,state,country} = allDetails;
     display.innerText=state+","+country;
     console.table(allDetails);
 })
   
}


function onerror(error)
{
if (error.code==1)
{
    display.innertext="you denied the request";
}
 else if (error.code==2)
{
    display.innertext="location not available";

}

else{
   display.innertext="something went wrong";
}
}
const form = document.getElementById('form')
const search = document.getElementById('search')
const result = document.getElementById('result')

/// api URL ///
const apiURL = 'https://apis.digital.gob.cl/fl/feriados';


///añadir el evento al form

form.addEventListener('submit', e=> {
    e.preventDefault();
    searchValue = search.value.trim()

    if(!searchValue){
        console.log("Ingrese año")
    }
    else{ 
        searchAño(searchValue)
    }
})


//buscar por año 
async function searchAño(){
    const searchResult = await fetch(`${apiURL}/${searchValue}`)
    const data = await searchResult.json();

    // console.log(finaldata)
    showData(data)
}






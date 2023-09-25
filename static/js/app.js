async function getAllapi()
{
    let apiUrls = [
        'api/mens',
        'api/womens',
        'api/kids',
        'api/accessories'
    ];
    let promises = apiUrls.map(URL=>fetch(URL).then(Response => Response.json()));

    Promise.all(promises).then(dataArray => {
        console.log(dataArray);
    }).catch(console => {
        console.error('Error:',error);
    });


getAllapi();
}

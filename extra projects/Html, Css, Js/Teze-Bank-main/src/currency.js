fetch("https://v6.exchangerate-api.com/v6/0a34f6f4e6751816d39180d0/latest/USD") // api with it's key
    .then(res => res.json())
    .then(res => {
        console.log(res);

        // Mail logic to create select tag with id and options. Options also have value
        const curDiv = (userObj, divToAppend, selectId) => {
            const newHtml = document.createElement("select"); // Creating select tah
            newHtml.id = selectId; // Setting id
            
            // Iterating over currencies object
            for (let cur in userObj) {
                const option = document.createElement("option");
                option.value = cur;
                option.textContent = `${cur} (${userObj[cur]})`;
                newHtml.appendChild(option);
            }
            divToAppend.appendChild(newHtml);
            // Adding select to specified place
        };

        // Creating 2 select tags
        curDiv(res.conversion_rates, document.getElementById("div1"), "select1");
        curDiv(res.conversion_rates, document.getElementById("div2"), "select2");


        // When form is submitted, we want to see result, so main logic is here
        document.getElementById('currency-form').addEventListener('submit', (e) => {
            e.preventDefault(); // Prevent form from resetting
            
            // For result:
            const fromCurrency = document.getElementById("select1").value;
            const toCurrency = document.getElementById("select2").value;
            const rates = res.conversion_rates;
            
            // If everything is working:
            if (fromCurrency && toCurrency) {
                const fromRate = rates[fromCurrency];
                const toRate = rates[toCurrency];
                const convertedValue = toRate / fromRate;

                // Finally, adding results
                document.getElementById("result").textContent = `Converted Value:  ${convertedValue.toFixed(2)} ${toCurrency}`; // toFixed is method for decimal places
                document.getElementById("res-label").textContent = `1 ${fromCurrency} = ${convertedValue.toFixed(2)} ${toCurrency}`;
            }
        });
    })
    .catch(error => alert('Error fetching exchange rates:', error)); // If any error happens
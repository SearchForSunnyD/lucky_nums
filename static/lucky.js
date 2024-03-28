const luck_form = $("#lucky-form");
const luck_result = $("#lucky-results");

/**
 * Handles the form submission, sends a POST request to the server,
 * and processes the response to display the results.
 * @param {Event} evt - The form submission event.
 */
async function processForm(evt) {
	evt.preventDefault();

	// Collect form data
	let formData = new FormData();
	$("#lucky-form input").each(function () {
		formData.append(this.id, $(this).val());
	});

	try {
		// Send POST request to the server
		const resp = await axios.post("/api/get-lucky-num", formData);

		// Process the server response
		handleResponse(resp.data);
	} catch (error) {
		console.error("Error processing form:", error);
	}
}

/**
 * Handles the response from the server, logs errors if any,
 * and creates cards for each item in the response.
 * @param {Object} data - The server response data.
 */
function handleResponse(data) {
	// Clear error fields before processing new response
	clearErrorFields();

	if (data.hasOwnProperty("errors")) {
		// Handle errors if present in the server response
		for (const err in data["errors"]) {
			let err_input = $(`#${err}-err`);

			// Clear existing error message
			err_input.text("");

			// Set the new error message
			err_input.text(data["errors"][err]);
		}
	} else {
		// If no errors, clear the result container and create cards
		luck_result.empty();
		for (const obj in data) {
			makeCard(data[obj][obj], data[obj]["fact"]);
		}
	}
}

/**
 * Creates a card with a heading and a paragraph based on the provided data
 * and appends it to the luck_result container.
 * @param {string} head - The heading for the card.
 * @param {string} text - The text content for the card.
 */
function makeCard(head, text) {
	const newDiv = document.createElement("div");
	const newHead = document.createElement("h3");
	const newP = document.createElement("p");

	newHead.innerText = head;
	newP.innerText = text;

	newDiv.append(newHead);
	newDiv.append(newP);

	luck_result.append(newDiv);
}

/**
 * Clears error fields associated with form inputs.
 */
function clearErrorFields() {
	// Assuming your error fields have IDs like "inputName-err"
	$("#lucky-form b[id$='-err']").text("");
}

// Set up the form submission event listener
luck_form.on("submit", processForm);

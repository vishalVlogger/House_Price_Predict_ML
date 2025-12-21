document.getElementById("predictForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData(e.target);
  const result = document.getElementById("result");

  try {
    const response = await fetch("/predict/", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    if (data.success) {
      const location =
        document.getElementById("location").options[
          document.getElementById("location").selectedIndex
        ].text;
      const sqft = document.getElementById("sqft").value;
      const bhk = document.getElementById("bhk").value;

      result.className = "success";
      result.innerHTML = `
                        <div style="font-size: 14px; margin-bottom: 8px;">
                            <strong>${bhk} BHK</strong> • ${sqft} sq.ft • ${location}
                        </div>
                        <div style="font-size: 16px; color: #28a745; margin-bottom: 5px;">
                            ✅ Estimated Price
                        </div>
                        <div class="price">${data.price_formatted}</div>
                    `;
    } else {
      result.className = "error";
      result.innerHTML = `❌ Error: ${data.error}`;
    }

    result.style.display = "block";
  } catch (error) {
    result.className = "error";
    result.innerHTML = `❌ Error: ${error.message}`;
    result.style.display = "block";
  }
});

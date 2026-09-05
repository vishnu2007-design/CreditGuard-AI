document.addEventListener("DOMContentLoaded", function () {
  const steps = document.querySelectorAll(".form-step");
  const progressSteps = document.querySelectorAll(".progress-step");
  const progressLines = document.querySelectorAll(".progress-line");

  const nextButtons = document.querySelectorAll(".next-btn");
  const prevButtons = document.querySelectorAll(".prev-btn");

  let currentStep = 0;

  // -----------------------------
  // Show Current Step
  // -----------------------------
  function showStep(step) {
    steps.forEach((item, index) => {
      item.classList.toggle("active", index === step);
    });

    progressSteps.forEach((item, index) => {
      item.classList.remove("active");
      item.classList.remove("completed");

      if (index === step) {
        item.classList.add("active");
      }

      if (index < step) {
        item.classList.add("completed");
      }
    });

    progressLines.forEach((line, index) => {
      if (index < step) {
        line.classList.add("completed");
      } else {
        line.classList.remove("completed");
      }
    });

    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }

  // -----------------------------
  // Validate Current Step
  // -----------------------------
  function validateStep() {
    const currentFormStep = steps[currentStep];

    const inputs = currentFormStep.querySelectorAll("input, select");

    for (let input of inputs) {
      if (!input.checkValidity()) {
        input.reportValidity();

        return false;
      }
    }

    return true;
  }

  // -----------------------------
  // Next Button
  // -----------------------------
  nextButtons.forEach((button) => {
    button.addEventListener("click", function () {
      if (!validateStep()) {
        return;
      }

      if (currentStep < steps.length - 1) {
        currentStep++;

        showStep(currentStep);

        // Calculate features when entering Review step
        if (currentStep === 4) {
          calculateFeatures();
        }
      }
    });
  });

  // -----------------------------
  // Previous Button
  // -----------------------------
  prevButtons.forEach((button) => {
    button.addEventListener("click", function () {
      if (currentStep > 0) {
        currentStep--;

        showStep(currentStep);
      }
    });
  });

  // -----------------------------
  // Calculate Engineered Features
  // -----------------------------
  function calculateFeatures() {
    // Payment amounts
    const payAmounts = [
      getNumber("PAY_AMT1"),
      getNumber("PAY_AMT2"),
      getNumber("PAY_AMT3"),
      getNumber("PAY_AMT4"),
      getNumber("PAY_AMT5"),
      getNumber("PAY_AMT6"),
    ];

    // Repayment delays
    const payDelays = [
      getNumber("PAY_0"),
      getNumber("PAY_2"),
      getNumber("PAY_3"),
      getNumber("PAY_4"),
      getNumber("PAY_5"),
      getNumber("PAY_6"),
    ];

    // Bill amounts
    const billAmounts = [
      getNumber("BILL_AMT1"),
      getNumber("BILL_AMT2"),
      getNumber("BILL_AMT3"),
      getNumber("BILL_AMT4"),
      getNumber("BILL_AMT5"),
      getNumber("BILL_AMT6"),
    ];

    // TOTAL_PAY_AMT
    const totalPay = payAmounts.reduce((sum, value) => sum + value, 0);

    // MAX_PAY_DELAY
    const maxDelay = Math.max(...payDelays);

    // TOTAL_BILL_AMT
    const totalBill = billAmounts.reduce((sum, value) => sum + value, 0);

    // Display calculated values
    const totalPayDisplay = document.getElementById("totalPayDisplay");

    const maxDelayDisplay = document.getElementById("maxDelayDisplay");

    const totalBillDisplay = document.getElementById("totalBillDisplay");

    if (totalPayDisplay) {
      totalPayDisplay.textContent = formatNumber(totalPay);
    }

    if (maxDelayDisplay) {
      maxDelayDisplay.textContent = formatNumber(maxDelay);
    }

    if (totalBillDisplay) {
      totalBillDisplay.textContent = formatNumber(totalBill);
    }
  }

  // -----------------------------
  // Get Number From Input
  // -----------------------------
  function getNumber(id) {
    const element = document.getElementById(id);

    if (!element || element.value === "") {
      return 0;
    }

    return Number(element.value);
  }

  // -----------------------------
  // Format Numbers
  // -----------------------------
  function formatNumber(number) {
    return new Intl.NumberFormat("en-IN", {
      maximumFractionDigits: 2,
    }).format(number);
  }

  // -----------------------------
  // Initialize
  // -----------------------------
  showStep(currentStep);
});

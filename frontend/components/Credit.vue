<template>
  <div>
    <iframe
      id="calcus-iframe-ipoteka"
      width="100%"
      height="300"
      frameborder="0"
      style="width: 1px; min-width: 100%"
      scrolling="no"
      src="https://calcus.ru/kalkulyator-ipoteki?embed=1"
      referrerpolicy="no-referrer-when-downgrade"
    ></iframe>
    <script>
      window.addEventListener("message", function (event) {
        if ((height_ipoteka = event.data["height_ipoteka"])) {
          document.getElementById("calcus-iframe-ipoteka").style.height =
            height_ipoteka + "px";
        }
      });
    </script>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>
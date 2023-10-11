<script>
    import Greeter from "./Greeter.svelte";
    import IoBox from "./IOBox.svelte";
    
</script>


<main class="m-auto flex lg:flex-row sm:flex-col justify-evenly items-center bg-teal-700 min-h-screen min-w-full">
  <Greeter />
  <IoBox />
</main>

<style>
  main {
    background-image: url("/background.svg");
    background-size: cover;
    background-position: center center;
  }
</style>

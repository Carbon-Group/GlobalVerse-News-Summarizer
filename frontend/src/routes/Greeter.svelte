<script>
  import { Badge } from "flowbite-svelte";
</script>

<svelte:head>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Zen+Dots&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Wallpoet&display=swap');
  </style>
</svelte:head>

<div id="greeting-container" class="flex items-center">
  <!-- TODO fix font imports -->
  <Badge
    rounded
    border
    color="bg-iocolor"
    class="font-header text-5xl dark:text-white dark:bg-transparent p-10 border-iocolor border-4"
    style="font-family: 'Zen Dots', cursive;">
      Welcome to the GlobalVerse!
  </Badge>
</div>

<style>

</style>

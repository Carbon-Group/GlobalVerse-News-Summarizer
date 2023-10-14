<script>
    import { getAnswer } from "$lib/func.js";
    import { writable } from "svelte/store";
    import { 
      Badge,
      Button,
      Card,
      Dropdown,
      DropdownItem,
      DropdownDivider,
      GradientButton,
      Spinner,
      Textarea,
      TextPlaceholder,
    } from 'flowbite-svelte';
    import { ChevronDownSolid, ClipboardSolid, CheckSolid} from 'flowbite-svelte-icons';
    const userOutput = writable("");
    // TODO убрать хардкод источника
    let sources = ["Источник не выбран", "futurism.com"];
    let selectedSource = sources[0];
    let currentState = "pre";
    let copied = false;
    async function showAnswer(source) {
      if (selectedSource === sources[0]) {
        alert("No source selected!");
        return;
      }
      currentState = "running";
      copied = false;
      userOutput.set(await getAnswer(selectedSource));
      currentState = "complete";
    }
    let dropdownOpen = false;
</script>


<!-- TODO декомпозировать этот большой компонент и наладить взаимодействие ввода и вывода -->
<div id="input-box" class="w-[25em]">
  <Button on:click color="bg-iocolor" class="w-full flex bg-iocolor justify-between">
    <Badge class="text-xl" color=blue>{selectedSource}</Badge>
    <ChevronDownSolid class="w-3 h-3 ml-2"/>
  </Button>
  <Dropdown bind:open={dropdownOpen} bind:value={selectedSource} class="w-full">
    {#each sources as source}
      <DropdownItem 
        class="w-[28em]"
        on:click={() => {selectedSource = source; dropdownOpen = false}}
        value={source}>{source}
      </DropdownItem>
      <DropdownDivider></DropdownDivider>
    {/each}
  </Dropdown>
  <GradientButton
    outline
    size="md"
    class="my-2 text-white bg-iocolor"
    on:click={() => showAnswer(selectedSource)}
    color=purpleToPink>
      <span class="font-bold text-xl">Parse!</span>
  </GradientButton>
</div>
<div id="output-box" class="w-[25em]">
    <Card class="max-w-full dark:bg-iocolor bg-iocolor mx-0">
      <h5 class="text-white text-xl mb-5">Полученная новость</h5>
      {#if currentState ==="running"}
        <Spinner color=white class="mr-3" size="6" />
        <TextPlaceholder size="sm" class="my-8" />
      {:else}
        <!-- TODO авто-ресайз окошка с текстом -->
        <Textarea readonly
          on:change={(e) => {currentState = "complete"; copied = false;}}
          class="font-normal text-white dark:text-white h-52"
          rows="auto"
          style="font-size: 1.125rem; line-height: 1.75rem;"
          value={$userOutput == "" ? "Пока ничего" : $userOutput}>
        </Textarea>
      {/if}
    {#if currentState === "complete"}
      <Button
        color=blue
        on:click={() => {navigator.clipboard.writeText($userOutput); copied = true}}
        class="top-full right-0 w-0 mt-2">
        {#if currentState === "complete" && !copied}
          <ClipboardSolid />
        {:else if currentState === "complete" && copied}
          <CheckSolid />
        {/if}
      </Button>
    {/if}
    </Card>
</div>

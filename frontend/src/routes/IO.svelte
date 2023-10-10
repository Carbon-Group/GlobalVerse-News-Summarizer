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
        Spinner,
    } from 'flowbite-svelte';
    import { ChevronDownSolid, ClipboardSolid, CheckSolid} from 'flowbite-svelte-icons';
    const userOutput = writable("");
    let sources = ["No source selected", "1"];
    let selectedSource = sources[0];
    let currentState = "pre";
    let copied = false;
    async function showAnswer(source) {
        if (selectedSource === sources[0]) {
            alert("No source selected!");
        }
        currentState = "running";
        copied = false;
        userOutput.set(await getAnswer(selectedSource));
        currentState = "complete";
    }

</script>

<div id="input-box" class="w-[25em]">

  <Button color=blue class="w-full flex justify-between">
    <Badge color=blue>{selectedSource}</Badge>
    <ChevronDownSolid class="w-3 h-3 ml-2"/>
  </Button>
  <Dropdown bind:value={selectedSource} class="w-full">
      {#each sources as source}
        <DropdownItem 
          class="w-[28em]"
          on:click={() => selectedSource = source}
          value={source}>{source}
        </DropdownItem>
        <DropdownDivider></DropdownDivider>
      {/each}
  </Dropdown>
  <Button color=blue class="my-2" on:click={() => showAnswer(selectedSource)}>Parse!</Button>
</div>
<div id="output-box" class="w-[25em]">
    <Card class="max-w-full dark:bg-sky-600 bg-sky-600 mx-0">
      {#if currentState ==="running"}
        <Spinner color=white class="mr-3" size="4" />
        <span class="text-white">Loading ...</span>
      {:else}
        <p 
          on:change={() => {currentState = "complete"; copied = false}}
          class="font-normal text-white dark:text-white leading-tight">
            {$userOutput == "" ? "Nothing here" : $userOutput}
        </p>
      {/if}
    {#if currentState === "complete"}
      <Button
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


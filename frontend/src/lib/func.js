import { client } from "@gradio/client";

export async function getAnswer(text) {
  const app = await client("http://127.0.0.1:7860/");
  const result = await app.predict(0, [
    "How to center a div in css?", // string  in 'Input text' Textbox component
  ]);
  console.log(result.data);
  return result.data[0];
}

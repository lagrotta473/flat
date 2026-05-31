import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';

const knowledgeBase = defineCollection({
  loader: glob({
    pattern: '**/*.md',
    base: '../knowledge_base',
  }),
});

const reunioes = defineCollection({
  loader: glob({
    pattern: '????-??-??_*.md',
    base: '../references/reunioes',
  }),
});

export const collections = { knowledgeBase, reunioes };

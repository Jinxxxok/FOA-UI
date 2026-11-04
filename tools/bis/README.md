# BIS 자료 만들기

1. SimulationCraft `profiles/MID2/*.simc` 와 `engine/dbc/generated/item_data.inc`, `spell_item_enchantment.inc` 를 받는다.
2. `parse.py` (SimC 프로필) → `guides.py` (SimC 프로필이 없는 전문화: 가이드 BIS 이름 → 아이템 ID) → `gen.py` 순서로 실행하면 `FOA_UI/BISData.lua` 가 만들어진다.
3. 시즌이 바뀌면 폴더 이름(MID2)과 가이드 목록만 바꿔서 다시 돌린다.

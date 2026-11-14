# FOA UI — First of All

월드 오브 워크래프트 **본섭(리테일)** 용 통합 UI 애드온입니다.

> 포에버(WoW Forever)용은 [foa-ui-forever](https://github.com/Jinxxxok/foa-ui-forever) 저장소를 쓰세요.

- 지원 버전: 리테일 12.1.x (인터페이스 120105 / 120100 / 120007)
- 설정: 게임 안에서 `/foa` 또는 ESC 메뉴의 **FOA UI** 버튼

## 설치

### WowUp으로 설치 (자동 업데이트 · 추천)
1. WowUp 위쪽에서 게임 버전을 **World of Warcraft (Retail)** 로 고릅니다.
2. **Get Addons(애드온 받기)** 에서 `FOA` 를 검색해 설치합니다.
   (검색에 아직 안 나오면 **Install from URL** 에 `https://github.com/Jinxxxok/FOA-UI` 를 넣어도 똑같이 설치됩니다.)
3. 새 버전이 올라오면 WowUp 에 업데이트가 뜹니다. **업데이트 → 게임 접속** 하면 끝입니다.

### 직접 설치
1. [Releases](https://github.com/Jinxxxok/foa-ui/releases) 에서 최신 `FOA_UI-vX.X.X.zip` 을 받습니다.
2. 압축을 풀어 나온 `FOA_UI` 폴더를 `World of Warcraft/_retail_/Interface/AddOns/` 에 넣습니다.
3. 캐릭터 선택 화면의 **애드온** 목록에서 드롭다운을 **모든 캐릭터** 로 두고 FOA UI 를 켭니다.

이미지(아이콘 / 글꼴)가 바뀐 버전으로 업데이트한 뒤에는 `/reload` 가 아니라 **게임을 완전히 껐다 켜야** 합니다.

## 주요 기능

| 구분 | 내용 |
|---|---|
| 화면 구성 | 가운데 체력·자원바, 직업 자원(연계 점수·신성한 힘·룬 등), 파티 / 레이드 프레임, 경험치 바 |
| 네임플레이트 | 적 체력·시전바·내 디버프, 정예(금)·희귀(은) 테두리, 역할 NPC 아이콘(상인·수리·은행·경매장·여관 등) |
| 가방 | 분류(고정 / 아이템 / 소모품 / 재료 / 잡동사니), 검색, 정리, 드래그 이동 |
| 미터기 | 블리자드 기본 데이터를 쓰는 피해량 / 치유량 미터기 + 위협(어그로) 미터 |
| 보스 알림 | 블리자드 보스 타임라인 / 경고를 FOA 디자인으로 |
| 편의 | 잡동사니 자동 판매, 자동 수리(길드 자금 우선), 튜토리얼 끄기, 새 주문 자동 배치 |
| 미니맵 | 애드온 버튼 목록(오른쪽 위), 파티 찾기 대기열 버튼(왼쪽 아래) |
| 편집 | 편집 모드로 위치 이동 — 위치는 **캐릭터별** 로 저장 |

## 명령어

| 명령어 | 기능 |
|---|---|
| `/foa` | 설정 창 |
| `/foa edit` | 편집 모드 (위치 옮기기) |
| `/foa test` | 테스트 모드 (파티·레이드·미터기·보스 알림 미리보기) |
| `/foa kb` | 빠른 단축키 설정 |
| `/foa reset` | 지금 캐릭터 위치 초기화 |
| `/foa log` | 막힌 동작 기록 보기 (오류 제보용) |

## 다른 애드온과 같이 쓸 때

FOA UI 와 같은 일을 하는 애드온과는 겹칩니다. 설정 창에서 해당 기능을 끄고 쓰세요.

- ElvUI 같은 통합 UI 와는 함께 쓰지 마세요.
- Plater → FOA 네임플레이트 끄기 · Bagnon → FOA 가방 끄기
- Details! → FOA 미터기 끄기 · DBM / BigWigs → FOA 보스 알림 끄기

## 오류 제보

오류가 나면 `/foa log` 화면과 함께 어떤 상황이었는지 알려 주세요.

## 라이선스

FOA UI 는 **GNU General Public License v3.0 (또는 그 이후 버전)** 으로 배포됩니다. 전문: [`LICENSE`](LICENSE) · `FOA_UI/LICENSE.txt`

고쳐서 다시 배포할 때도 GPL-3.0 을 따라야 하고, 소스를 함께 공개해야 합니다. 퀘스트 자료 일부가 GPL-3.0 인 QuestieDB 에서 왔기 때문입니다 (아래 자료 출처).

## 사용한 자료와 라이선스

- 글꼴: IBM Plex Sans KR, Inter, Space Grotesk — SIL Open Font License 1.1 (`FOA_UI/Media/Fonts` 에 라이선스 포함)
- 아이콘: Lucide — ISC License (`FOA_UI/Media/Icons/LICENSE-lucide.txt`)

## 자료 출처

- 던전 보스 · 전리품, 퀘스트 · 비행 지점 자료: [AllTheThings](https://github.com/ATTWoWAddon/AllTheThings) (MIT License · `FOA_UI/LICENSE-AllTheThings.txt`)
- 던전 한글 이름 · 권장 레벨 · 보스 순서, 직업 기술 레벨, 전문기술 빠른 레벨링 경로, 특성 레벨업 순서: [wowf.io](https://wowf.io/ko)
- 퀘스트 선행 · 택일 · 연결 퀘스트 · 조건(숙련도 · 평판 · 레벨) · 보고 NPC 와 자리: [QuestieDB](https://github.com/Questie/QuestieDB) 포에버 합본 자료 (GPL-3.0 · 포에버 실제 플레이 기록으로 확인한 선행 관계 포함 · `FOA_UI/LICENSE-QuestieDB.txt` · 만드는 방법은 `tools/quests/questie_export.py` → `tools/quests/gen_quests.py`)
- 포에버에서 바뀐 지도 경계(스톰윈드 · 동부 역병지대 · 멀고어 · 붉은마루 산맥) 변환식: QuestieDB 자료와 대조해 확인 (`tools/maps/forever_frame_fixes.json`)
- 아이콘: [Lucide](https://lucide.dev) (ISC License · `FOA_UI/Media/Icons/LICENSE-lucide.txt`)

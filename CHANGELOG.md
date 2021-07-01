# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-speech/#history

## [2.5.0](https://www.github.com/googleapis/python-speech/compare/v2.4.1...v2.5.0) (2021-07-01)


### Features

* add always_use_jwt_access ([#191](https://www.github.com/googleapis/python-speech/issues/191)) ([0d84445](https://www.github.com/googleapis/python-speech/commit/0d8444543138f45445fc7995eccd5655376e0bfc))

### [2.4.1](https://www.github.com/googleapis/python-speech/compare/v2.4.0...v2.4.1) (2021-06-21)


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-speech/issues/1127)) ([#178](https://www.github.com/googleapis/python-speech/issues/178)) ([77d8d0e](https://www.github.com/googleapis/python-speech/commit/77d8d0ebc9924f965b86d3196e73170f875dd06f)), closes [#1126](https://www.github.com/googleapis/python-speech/issues/1126)

## [2.4.0](https://www.github.com/googleapis/python-speech/compare/v2.3.0...v2.4.0) (2021-05-22)


### Features

* add webm opus support ([eb360ae](https://www.github.com/googleapis/python-speech/commit/eb360aefdac09648852a073ef0837dc7c7b18679))
* support self-signed JWT flow for service accounts ([eb360ae](https://www.github.com/googleapis/python-speech/commit/eb360aefdac09648852a073ef0837dc7c7b18679))


### Bug Fixes

* add async client to %name_%version/init.py ([eb360ae](https://www.github.com/googleapis/python-speech/commit/eb360aefdac09648852a073ef0837dc7c7b18679))

## [2.3.0](https://www.github.com/googleapis/python-speech/compare/v2.2.1...v2.3.0) (2021-04-08)


### Features

* Support for spoken punctuation and spoken emojis ([#143](https://www.github.com/googleapis/python-speech/issues/143)) ([b6bddbe](https://www.github.com/googleapis/python-speech/commit/b6bddbe46172debd962c3d8e566a7c410fb4f279))

### [2.2.1](https://www.github.com/googleapis/python-speech/compare/v2.2.0...v2.2.1) (2021-03-31)


### Bug Fixes

* use correct retry deadline ([#134](https://www.github.com/googleapis/python-speech/issues/134)) ([07a30a1](https://www.github.com/googleapis/python-speech/commit/07a30a18ab4e38cca46af905cfd4221ce06daeb3))

## [2.2.0](https://www.github.com/googleapis/python-speech/compare/v2.1.0...v2.2.0) (2021-03-19)


### Features

* adds model adaptation sample ([#121](https://www.github.com/googleapis/python-speech/issues/121)) ([24b9424](https://www.github.com/googleapis/python-speech/commit/24b94247bab22b8fad15a251bff06ec8620f0f90))
* Support output transcript to Google Cloud Storage for LongRunningRecognize ([#128](https://www.github.com/googleapis/python-speech/issues/128)) ([5974564](https://www.github.com/googleapis/python-speech/commit/59745644b08328c883e71d53f3fcc5537644e3c7))

## [2.1.0](https://www.github.com/googleapis/python-speech/compare/v2.0.1...v2.1.0) (2021-02-26)


### Features

* add common resource helpers; expose transport; remove gRPC send/recv limits ([#100](https://www.github.com/googleapis/python-speech/issues/100)) ([b4700a6](https://www.github.com/googleapis/python-speech/commit/b4700a60569cb917f176ae1f504dadac1edb6ae8))
* add from_service_account_info factory ([3bed0b4](https://www.github.com/googleapis/python-speech/commit/3bed0b43c75be649e29475240c7f486fc9cd63dc))
* adds new multi region sample ([#96](https://www.github.com/googleapis/python-speech/issues/96)) ([a103f09](https://www.github.com/googleapis/python-speech/commit/a103f09fe6173f3acd8402f8c2a669ea3001ac6f))
* **v1p1beta1:** support Model Adaptation ([#104](https://www.github.com/googleapis/python-speech/issues/104)) ([3bed0b4](https://www.github.com/googleapis/python-speech/commit/3bed0b43c75be649e29475240c7f486fc9cd63dc))


### Bug Fixes

* Remove incorrect comment on enhanced models ([#95](https://www.github.com/googleapis/python-speech/issues/95)) ([8a02cee](https://www.github.com/googleapis/python-speech/commit/8a02ceeb5723b4d5075ab90bf64edefae9b81572))


### Documentation

* fix sphinx identifiers ([3bed0b4](https://www.github.com/googleapis/python-speech/commit/3bed0b43c75be649e29475240c7f486fc9cd63dc))
* updated setup documentation to point to python-speech instead of python-docs-samples ([#89](https://www.github.com/googleapis/python-speech/issues/89)) ([722e86e](https://www.github.com/googleapis/python-speech/commit/722e86e726831f7e44dbc8f0fb620a1ccd45f116))

### [2.0.1](https://www.github.com/googleapis/python-speech/compare/v2.0.0...v2.0.1) (2020-11-16)


### Bug Fixes

* deleted a line duplicating the call to the recognizer  ([#83](https://www.github.com/googleapis/python-speech/issues/83)) ([3ef6ce5](https://www.github.com/googleapis/python-speech/commit/3ef6ce5796126847acf231f67e2a2c9b52e27f5a))
* migrated samples to speech 2.0.0 ([#78](https://www.github.com/googleapis/python-speech/issues/78)) ([47dd992](https://www.github.com/googleapis/python-speech/commit/47dd99237d79f7e7b991f6a15733c6e04b00f563))

## [2.0.0](https://www.github.com/googleapis/python-speech/compare/v1.3.2...v2.0.0) (2020-09-24)


### ⚠ BREAKING CHANGES

* migrate to microgenerator (#61)

### Features

* Migrate to microgenerator ([#61](https://www.github.com/googleapis/python-speech/issues/61)) ([283b49d](https://www.github.com/googleapis/python-speech/commit/283b49d2cb34dcfcbd12038582ca3ed37e5ab90b)). See the [migration guide](https://github.com/googleapis/python-speech/blob/release-v2.0.0/UPGRADING.md) for details.


### Documentation

* remove example usage from READMe ([#46](https://www.github.com/googleapis/python-speech/issues/46)) ([4214630](https://www.github.com/googleapis/python-speech/commit/4214630c3318e6c9bc0a5156e20344956faf7d52))

### [1.3.2](https://www.github.com/googleapis/python-speech/compare/v1.3.1...v1.3.2) (2020-02-03)


### Bug Fixes

* **speech:** increase default timeout for v1p1beta1 (via synth) ([#9999](https://www.github.com/googleapis/python-speech/issues/9999)) ([e9b4919](https://www.github.com/googleapis/python-speech/commit/e9b4919f493a9206406944093fc1c3408b5f0265))
* **speech:** increase timeout values in client config (via synth) ([#9922](https://www.github.com/googleapis/python-speech/issues/9922)) ([8d34bea](https://www.github.com/googleapis/python-speech/commit/8d34beab73273e1b0965fe622af5434fdbac01ca))
* **speech:** mark `Recognize` idempotent (via synth) ([#9874](https://www.github.com/googleapis/python-speech/issues/9874)) ([a69e08c](https://www.github.com/googleapis/python-speech/commit/a69e08ce0bafcd9c4f1bafe51dce6e6b4716994f))
* **speech:** move 'speaker_tag' field from 'SpeakerDiarizationConfig' to 'WordInfo' (via synth) ([#9576](https://www.github.com/googleapis/python-speech/issues/9576)) ([2ba5ab9](https://www.github.com/googleapis/python-speech/commit/2ba5ab969e09df5cafcf67861c9d7d6cc91bd0ca))
* **speech:** re-add unused speaker_tag; update spacing in docs templates (via synth) ([#9765](https://www.github.com/googleapis/python-speech/issues/9765)) ([e1c5a54](https://www.github.com/googleapis/python-speech/commit/e1c5a54a321f5e76f074f8be1f5b6d5aedd612c7))

## 1.3.1

12-06-2019 13:05 PST

### Implementation Changes
- Increase timeout values in client config (via synth). ([#9922](https://github.com/googleapis/google-cloud-python/pull/9922))

## 1.3.0

11-21-2019 14:03 PST


### Implementation Changes
- Mark `Recognize` as idempotent (via synth). ([#9874](https://github.com/googleapis/google-cloud-python/pull/9874))
- Re-add unused `speaker_tag`; update spacing in docs templates (via synth). ([#9765](https://github.com/googleapis/google-cloud-python/pull/9765))
- Move `speaker_tag` field from `SpeakerDiarizationConfig` to `WordInfo` (via synth). ([#9576](https://github.com/googleapis/google-cloud-python/pull/9576))
- Remove send/recv msg size limit (via synth). ([#8969](https://github.com/googleapis/google-cloud-python/pull/8969))

### New Features
- Add speaker diarization configuration support (via synth). ([#9202](https://github.com/googleapis/google-cloud-python/pull/9202))
- Add `SpeakerDiarizationConfig`, deprecate enable_speaker_diarization and diarization_speaker_count (via synth). ([#8795](https://github.com/googleapis/google-cloud-python/pull/8795))

### Documentation
- Add python 2 sunset banner to documentation. ([#9036](https://github.com/googleapis/google-cloud-python/pull/9036))
- Reorder samples. ([#9313](https://github.com/googleapis/google-cloud-python/pull/9313))
- Update docstrings (via synth). ([#9292](https://github.com/googleapis/google-cloud-python/pull/9292))
- Fix intersphinx reference to requests. ([#9294](https://github.com/googleapis/google-cloud-python/pull/9294))
- Add generated code samples. ([#9153](https://github.com/googleapis/google-cloud-python/pull/9153))
- Remove CI for gh-pages, use googleapis.dev for `api_core` refs. ([#9085](https://github.com/googleapis/google-cloud-python/pull/9085))
- Remove compatibility badges from READMEs. ([#9035](https://github.com/googleapis/google-cloud-python/pull/9035))
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))

### Internal / Testing Changes
- Add v1p1beta1 systests for longrunning / streaming recognize. ([#9287](https://github.com/googleapis/google-cloud-python/pull/9287))
- Add v1 systests for longrunning / streaming recognize. ([#9285](https://github.com/googleapis/google-cloud-python/pull/9285))
- Update samples manifest (via synth). ([#9211](https://github.com/googleapis/google-cloud-python/pull/9211))

## 1.2.0

07-24-2019 17:35 PDT

### New Features
- Add 'client_options' support (via synth). ([#8534](https://github.com/googleapis/google-cloud-python/pull/8534))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))
- Pin black version (via synth). ([#8596](https://github.com/googleapis/google-cloud-python/pull/8596))

### Documentation
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))

## 1.1.0

06-27-2019 16:55 PDT

### Implementation Changes
- Allow kwargs to be passed to 'create_channel' (via synth). ([#8428](https://github.com/googleapis/google-cloud-python/pull/8428))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))

### New Features
- Increase speech max received msg size to 256 MiB ([#8338](https://github.com/googleapis/google-cloud-python/pull/8338))
- Add MP3 to Audio Encoding and add boost to Speech Context (via synth). ([#8109](https://github.com/googleapis/google-cloud-python/pull/8109))
- Add Recognition Metadata (via synth). ([#7961](https://github.com/googleapis/google-cloud-python/pull/7961))

### Documentation
- Update to show 'google-cloud-speech' is GA. ([#8453](https://github.com/googleapis/google-cloud-python/pull/8453))
- Tweak 'SpeechContext' docstring (via synth). ([#8223](https://github.com/googleapis/google-cloud-python/pull/8223))

### Internal / Testing Changes
- All: Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))
- (Re)-blacken (via synth). ([#8446](https://github.com/googleapis/google-cloud-python/pull/8446))
- Add disclaimer to auto-generated template files (via synth).  ([#8328](https://github.com/googleapis/google-cloud-python/pull/8328))
- Suppress checking 'cov-fail-under' in nox default session (via synth).  ([#8252](https://github.com/googleapis/google-cloud-python/pull/8252))
- Fix coverage in 'types.py' (via synth). ([#8164](https://github.com/googleapis/google-cloud-python/pull/8164))
- Blacken noxfile.py, setup.py (via synth). ([#8132](https://github.com/googleapis/google-cloud-python/pull/8132))
- Add empty lines. ([#8072](https://github.com/googleapis/google-cloud-python/pull/8072))
- Update noxfile (via synth). ([#7836](https://github.com/googleapis/google-cloud-python/pull/7836))
- Add nox session `docs` (via synth). ([#7782](https://github.com/googleapis/google-cloud-python/pull/7782))

## 1.0.0

03-18-2019 08:05 PDT


### Implementation Changes
- Remove unused message exports. ([#7275](https://github.com/googleapis/google-cloud-python/pull/7275))

### New Features
- Promote google-cloud-speech to GA ([#7525](https://github.com/googleapis/google-cloud-python/pull/7525))

### Documentation
- Updated client library documentation URLs. ([#7307](https://github.com/googleapis/google-cloud-python/pull/7307))

### Internal / Testing Changes
- Speech: copy lintified proto files (via synth).
- Add clarifying comment to blacken nox target. ([#7404](https://github.com/googleapis/google-cloud-python/pull/7404))
- Copy proto files alongside protoc versions. Remove unneeded utf-8 header.

## 0.36.3

01-31-2019 09:57 PST


### New Features
- Add 'RecognitionConfig.audio_channel_count' field via synth. ([#7240](https://github.com/googleapis/google-cloud-python/pull/7240))

### Documentation
- Modify file headers. ([#7158](https://github.com/googleapis/google-cloud-python/pull/7158))

### Internal / Testing Changes
- Add protos as an artifact to library ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))

## 0.36.2

01-10-2019 15:36 PST

### Implementation Changes
- Protoc-generated serialization update. ([#7106](https://github.com/googleapis/google-cloud-python/pull/7106))

### Documentation
- Regenerate speech to change quote chars in docstr.
- Pick up stub docstring fix in GAPIC generator. ([#6982](https://github.com/googleapis/google-cloud-python/pull/6982))

## 0.36.1

12-18-2018 09:46 PST


### Implementation Changes
- Import `iam.policy` from `google.api_core`. ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))
- Pick up fixes to GAIPC generator. ([#6508](https://github.com/googleapis/google-cloud-python/pull/6508))
- Add `result_end_time`, docstring changes via synth. ([#6462](https://github.com/googleapis/google-cloud-python/pull/6462))
- Assorted synth fixups / cleanups ([#6400](https://github.com/googleapis/google-cloud-python/pull/6400))
- Fix `client_info` bug, update docstrings and timeouts. ([#6421](https://github.com/googleapis/google-cloud-python/pull/6421))
- Re-generate library using speech/synth.py ([#5979](https://github.com/googleapis/google-cloud-python/pull/5979))

### Dependencies
- Bump minimum `api_core` version for all GAPIC libs to 1.4.1. ([#6391](https://github.com/googleapis/google-cloud-python/pull/6391))

### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Clarify passed arguments in speech examples. ([#6857](https://github.com/googleapis/google-cloud-python/pull/6857))
- Docs: normalize use of support level badges ([#6159](https://github.com/googleapis/google-cloud-python/pull/6159))
- Fix client library URL. ([#6052](https://github.com/googleapis/google-cloud-python/pull/6052))
- Prep docs for repo split. ([#6017](https://github.com/googleapis/google-cloud-python/pull/6017))

### Internal / Testing Changes
- Synth.metadata. ([#6868](https://github.com/googleapis/google-cloud-python/pull/6868))
- Update noxfile.
- Blacken all gen'd libs ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- Omit local deps ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Run Black on Generated libraries ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))
- Add / fix badges for PyPI / versions. ([#6158](https://github.com/googleapis/google-cloud-python/pull/6158))
- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))

## 0.36.0

### New Features

- Re-generate the library to pick up changes and new features in the underlying API. ([#5915](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5915))

### Documentation

- Fix broken links to description of 'Beta' ([#5917](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5917))
- Replace links to '/stable/' with '/latest/'. ([#5901](https://github.com/GoogleCloudPlatform/google-cloud-python/pull/5901))

## 0.35.0

### Implementation Changes

- Re-generated the library to pick up new API features. (#5577)

### Internal / Testing Changes

- Add Test runs for Python 3.7 and remove 3.4 (#5295)
- Avoid overwriting '__module__' of messages from shared modules. (#5364)
- Modify system tests to use prerelease versions of grpcio (#5304)

## 0.34.0

### Implementation Changes
- Regenerate GAPIC to account for the removal of GoogleDataCollectionConfig and google_data_collection_opt_in  (#5235)

## 0.33.0

### New Features

- Add Audio Logging and Recognition Metadata. (#5123)

### Internal / Testing Changes

- Fix bad trove classifier

## 0.32.1

### Dependencies

- Update dependency range for api-core to include v1.0.0 releases (#4944)

### Testing and internal changes

- Install local dependencies when running lint (#4936)
- Re-enable lint for tests, remove usage of pylint (#4921)
- Normalize all setup.py files (#4909)

## 0.31.1

### Bugfixes

- Fix speech helpers to properly pass retry and timeout args. (#4828, #4830)

## 0.31.0

This is the (hopefully) final release candidate before 1.0.

### Breaking Changes

- The deprecated Speech layer (deprecated since 0.27.0) has been removed. If you are still using  it, the [migration guide](https://cloud.google.com/speech/docs/python-client-migration) is still available.
- The following changes are _technically_ breaking but very unlikely to affect you directly:
  * `google.cloud.gapic.speech.v1` moved to `google.cloud.speech_v1.gapic`, in accordance with more recent clients.
  * `google.cloud.proto.speech.v1` moved to `google.cloud.speech_v1.proto`, in accordance with more recent clients.

### Dependencies

  * Removed dependency on `google-gax`.
  * Added dependency on `google-api-core`, its replacement.

## 0.30.0

### Documentation

- Added link to "Python Development Environment Setup Guide" in
  project README (#4187, h/t to @michaelawyu)

### Dependencies

- Upgrading to `google-cloud-core >= 0.28.0` and adding dependency
  on `google-api-core` (#4221, #4280)
- Deferring to `google-api-core` for `grpcio` and
  `googleapis-common-protos`dependencies (#4096, #4098)

PyPI: https://pypi.org/project/google-cloud-speech/0.30.0/
